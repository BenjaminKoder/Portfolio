package project;

import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

import project.persistence.GameInformation;

public class GameInformationTest {
    @Test
    public void validUsername(){
        assertThrows(IllegalArgumentException.class, () ->{
            new GameInformation(null, 0);
        });
        assertThrows(IllegalArgumentException.class, () -> {
            new GameInformation("", 0);
        });
    }
    @Test
    public void validPassword(){
        assertThrows(IllegalArgumentException.class, () -> {
            new GameInformation("Benjamin", -5);
        });
    }
}
