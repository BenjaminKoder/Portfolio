package project.controllers;

import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Optional;
import java.util.ResourceBundle;
import java.util.Set;

import javafx.animation.AnimationTimer;
import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.ButtonType;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.KeyCode;
import javafx.scene.layout.AnchorPane;
import javafx.scene.shape.Rectangle;
import javafx.scene.text.Text;
import project.ProsjektApp;
import project.game.GameState;
import project.game.GameStateObserver;
import project.game.GrassPlatform;
import project.game.Player;
import project.persistence.GameInformation;
import project.persistence.GameLoaderInterface;
import project.persistence.HomeFolderLoader;

public class GameController implements GameStateObserver, Initializable{
    @FXML private AnchorPane anchorPaneGame, playerPane, grassplatformPane;
    @FXML private ImageView grassplatformView;
    @FXML private Button menuButton;
    @FXML private Rectangle playerRect, grassplatformRect;
    @FXML private Text textScore, textHighscore;
    @FXML private Image crackedPlatform = new Image(getClass().getResourceAsStream("/project/2dplatformerCrackedBenjamin.png"));
    @FXML private Image normalPlatform = new Image(getClass().getResourceAsStream("/project/2dplatformerBenjamin.png"));
    @FXML private Image rightPlayer = new Image(getClass().getResourceAsStream("/project/2dcharacterBenjamin.png"));
    @FXML private Image leftPlayer = new Image(getClass().getResourceAsStream("/project/2dcharacterLeftBenjamin.png"));


    private Player player;
    // private boolean initializedGame = false;

    // Problemet ligger her: gameState starter ikke å kjøre før anchorPane har loadet, men anchorPane kjører ikke på repeat fordi gameState ikke har startet. Spør chat
    private GameState gameState;
    private List<AnchorPane> grassplatformPanes = new ArrayList<>();
    private AnimationTimer gameLoop;

    private final Set<KeyCode> activeKeys = new HashSet<>();

    private Alert alert;
    private boolean alertShown;
    private String username;

   @FXML
    public void switchSceneMenu(ActionEvent event) throws IOException{
        this.shutdown();
        ProsjektApp.setRoot("Menu");
    }
    
    @FXML 
    public void updateUI(){
        while (grassplatformPanes.size() > gameState.getPlatforms().size()) {
            AnchorPane pane = grassplatformPanes.remove(grassplatformPanes.size() - 1);
            anchorPaneGame.getChildren().remove(pane);
        }
        for (int i = 0; i < this.gameState.getPlatforms().size(); i++) {
            GrassPlatform p = this.gameState.getPlatforms().get(i);
            AnchorPane grassplatformPane = grassplatformPanes.get(i); 
            grassplatformPane.setLayoutX(p.getXPos());
            grassplatformPane.setLayoutY(p.getYPos());
            for (Node node : grassplatformPane.getChildren()) {
                if (node instanceof ImageView) {
                    ((ImageView) node).setImage(p.getCrackedPlatform() ? crackedPlatform : normalPlatform);
                }
            }
        }
        this.playerPane.setLayoutX(this.player.getXPos());
        this.playerPane.setLayoutY(this.player.getYPos());
        this.textScore.setText(String.valueOf(this.gameState.getScore()));
        this.textHighscore.setText("Highscore: "+String.valueOf(this.gameState.getHighscore()));
        if(this.gameState.isGameOver() && !this.alertShown){
            this.alertShown = true;
            Platform.runLater(() -> {
                gameState.setHighscore();

                this.alert = new Alert(Alert.AlertType.CONFIRMATION);
                this.alert.setContentText("You got a score of "+this.gameState.getScore()+"!");
                this.alert.setTitle("Game Over");
                this.alert.setHeaderText("You Lost!");
                
                ButtonType restartButton = new ButtonType("Play Again");
                alert.getButtonTypes().setAll(restartButton);

                Optional<ButtonType> result = alert.showAndWait();

                if (result.isPresent() && result.get() == restartButton) {
                    resetGame(); 
                } 
                });
        }

    }
    private void startGameLoop() {
        gameLoop = new AnimationTimer() {
            // Kjører 60 ganger per sek:
            @Override
            public void handle(long now) {
                gameState.run(); 
                if(activeKeys.contains(KeyCode.A)||activeKeys.contains(KeyCode.LEFT)){
                    gameState.movePlayerLeft();
                    for (Node node : playerPane.getChildren()) {
                        if (node instanceof ImageView) {
                            ((ImageView) node).setImage(leftPlayer);
                        }
                    }
                }
                else if(activeKeys.contains(KeyCode.D)||activeKeys.contains(KeyCode.RIGHT)){
                    gameState.movePlayerRight();
                    for (Node node : playerPane.getChildren()) {
                        if (node instanceof ImageView) {
                            ((ImageView) node).setImage(rightPlayer);
                        }
                    }
                }
                
            }
        };
        gameLoop.start();
    }
    @FXML
    // Handle-metoden kjøres hver gang det skjer en endring hos objektene. Dette ønsker jeg å legge til ved å bruke 
    public void handle() {
        this.updateUI();
    }
    @Override
    public void initialize(URL location, ResourceBundle resources) {
        Platform.runLater(() -> {
            anchorPaneGame.requestFocus();
            anchorPaneGame.setOnKeyPressed(e->activeKeys.add(e.getCode()));
            anchorPaneGame.setOnKeyReleased(e->{
                activeKeys.remove(e.getCode());
                this.gameState.setPlayerIsMoving(false);
            });
        });
        this.player = new Player(150, 200, this.playerRect.getWidth(), this.playerRect.getHeight());
        this.gameState = new GameState(player);
        this.grassplatformPanes = new ArrayList<>();
        this.gameState.generateRandomPlatforms(5);

        this.gameState.getPlatforms().stream().forEach(p->{
            AnchorPane newGrassplatformPane = new AnchorPane();
            ImageView newImageView = new ImageView(this.grassplatformView.getImage());
            newImageView.setFitWidth(this.grassplatformView.getFitWidth());
            newImageView.setFitHeight(this.grassplatformView.getFitHeight());
            newGrassplatformPane.getChildren().add(newImageView);
            newGrassplatformPane.setLayoutX(p.getXPos());
            newGrassplatformPane.setLayoutY(p.getYPos());
            if(p.getCrackedPlatform()){
                // I want to change the image of the imageview thats under the grassplatformpane to the cracked platform image in my resources folder.
                for (Node node : newGrassplatformPane.getChildren()){
                    if(node instanceof ImageView){
                        ((ImageView) node).setImage(crackedPlatform);
                    }
                }
            }else{
                for (Node node : newGrassplatformPane.getChildren()){
                    if(node instanceof ImageView){
                        ((ImageView) node).setImage(normalPlatform);
                    }
                }
            }
            anchorPaneGame.getChildren().add(newGrassplatformPane);
            this.grassplatformPanes.add(newGrassplatformPane);
            newGrassplatformPane.toBack();
        });
        this.alertShown = false;
        this.gameState.addListener(this);
        this.startGameLoop();
        this.updateUI();
    }
    public void resetGame(){
 
        this.player.setXPos(150); 
        this.player.setYPos(200); 
        this.gameState.setVelocity(0, 0);
        this.activeKeys.clear();

        this.textHighscore.setText("Highscore: "+String.valueOf(this.gameState.getHighscore()));
        this.gameState.setScore(0);
        this.textScore.setText("0");

        this.gameState.clearPlatforms(); 
        this.gameState.generateRandomPlatforms(5);

        this.gameState.setGameOver(false);

        this.alertShown = false;
        this.updateUI();
    }
    public void shutdown(){
        this.gameState.setHighscore();
        GameInformation gameInformation = new GameInformation(this.username, this.gameState.getHighscore());
        GameLoaderInterface gameLoader = new HomeFolderLoader();
        gameLoader.save(gameInformation);
    }
    public void setUsername(String username){
        if(username.isEmpty()){
            throw new IllegalArgumentException("Username cannot be null");
        }
        this.username = username;
    }
    public void loadHighscore(int loadedHighscore){
        this.gameState.loadHighscore(loadedHighscore);
    }

}
