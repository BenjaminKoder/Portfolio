package project;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import project.game.GameObject;

public class GameObjectTest {
    @Test
    public void widthAndXPosTest(){
        GameObject player = new GameObject(10,10,-10,10);
        assertEquals(100,player.getWidth());
        assertEquals(10, player.getXPos());
    }
}
