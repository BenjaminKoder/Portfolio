package project.persistence;

import java.io.IOException;

public interface GameLoaderInterface {
    void save(GameInformation gameInformation);
    GameInformation load(String username) throws IOException;
}
