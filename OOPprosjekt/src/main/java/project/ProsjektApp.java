package project;


import java.io.IOException;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent; 
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.util.Pair;
import project.controllers.GameController;

public class ProsjektApp extends Application{

    private static Object controller;

    private static Scene SCENE;
    public static void main(String[] args) {
        Application.launch(args);
    }

    @Override
    public void start(Stage primaryStage) throws IOException {
        try {
            Pair<Parent, Object> loaded = loadFXML("Menu");
            SCENE = new Scene(loaded.getKey());
            controller = loaded.getValue();
            primaryStage.setTitle("Jumpy jump"); 
            primaryStage.setScene(SCENE);
            primaryStage.show();

            primaryStage.setOnHidden(e->{
                if(controller instanceof GameController){
                    ((GameController) controller).shutdown();
                }
            });
        }
        catch (Exception e){
            e.printStackTrace();
        }
    }
    public static Object setRoot(String fxml) throws IOException{
        Pair<Parent, Object> loaded = loadFXML(fxml);
        SCENE.setRoot(loaded.getKey()); 
        controller = loaded.getValue();
        return controller;
    }
    public static <T> Pair<Parent, T> loadFXML(String fxml) throws IOException{
        FXMLLoader fxmlLoader = new FXMLLoader(ProsjektApp.class.getResource(fxml+ ".fxml"));
        return new Pair<>(fxmlLoader.load(), fxmlLoader.getController());
    }
}