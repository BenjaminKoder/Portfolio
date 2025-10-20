package project.controllers;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;
import project.ProsjektApp;
import project.persistence.GameInformation;
import project.persistence.GameLoaderInterface;
import project.persistence.HomeFolderLoader;
import project.user.User;
import project.user.UserManager;

public class ProsjektController implements Initializable{
    private String username;
    private String password;
    private UserManager userManager = new UserManager();
    

    @FXML private AnchorPane anchorPaneMenu;
    @FXML private Button logInButton, signUpButton;
    @FXML private PasswordField passwordField;
    @FXML private TextField usernameField;
    @FXML private TextArea textArea;
    @FXML private Stage stage;
    @FXML
    public void switchSceneGame() throws IOException{
        GameController gameController =(GameController) ProsjektApp.setRoot("Game");
        gameController.setUsername(this.username);
        GameLoaderInterface homeFolderLoader = new HomeFolderLoader();
        GameInformation gameInformation = homeFolderLoader.load(this.username);
        gameController.loadHighscore(gameInformation.getHighscore());
    }

    @FXML
    public void handleLogIn() throws IOException {
        this.username = usernameField.getText().trim();
        this.password = passwordField.getText();
        if(this.username.isEmpty() || this.password.isEmpty()){
            this.textArea.setText("Username- and password-fields cannot be empty!");
        }
        else if(this.userManager.userHasAccount(new User(this.username,this.password))){
            switchSceneGame();
        }else{
            this.textArea.setText("Username and/or password is incorrect");
        }
    } 
    @FXML
    public void handleSignUp() throws IOException{
        this.username = usernameField.getText().trim();
        this.password = passwordField.getText();
        User user = new User(this.username,this.password);
        // Bryr oss ikke mye om passord. Finnes brukernavnet, så skal man logge inn i stedet. Finnes ikke brukernavnet, lager man en ny konto med riktig brukernavn og passord.
        if(this.username.isEmpty() || this.password.isEmpty()){
            this.textArea.setText("Username- and password-fields cannot be empty!");
        }
        else if(this.userManager.usernameExists(user)){
            this.textArea.setText("Account already exists, log in instead. Password may still be wrong.");
        }else if(this.username.contains(";")){
            this.textArea.setText("Username cannot include ';'");
        }
        else{
            this.userManager.addUser(new User(this.username, this.password));
            switchSceneGame();
        }
    }

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        Platform.runLater(() -> anchorPaneMenu.requestFocus());
    }
    
    
}
