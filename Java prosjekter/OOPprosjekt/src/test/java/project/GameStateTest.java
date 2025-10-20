package project;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import project.game.GameState;
import project.game.Player;

public class GameStateTest {
    @Test
    public void highscoreTest(){
        GameState gameState = new GameState(new Player(100,100, 100, 100));
        assertEquals(0, gameState.getHighscore());
        gameState.loadHighscore(100);
        assertEquals(100, gameState.getHighscore());
        gameState.loadHighscore(99);
        assertEquals(99, gameState.getHighscore());
    }
}
