package project.persistence;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class HomeFolderLoader implements GameLoaderInterface {

    private File saveFile;

    public HomeFolderLoader() {
        String path = System.getProperty("user.home") + File.separator + "JumpyJump" + File.separator + "save.txt";
        this.saveFile = new File(path);
    }

    @Override
    public GameInformation load(String username) throws IOException{
        if(!this.saveFile.exists()){
            this.saveFile.createNewFile();
        }
        int highscore = 0;
        try (Scanner scanner = new Scanner(this.saveFile)){
            String line;
            while(scanner.hasNext()){
                line = scanner.nextLine();
                String[] lineList = line.split(";");
                if(lineList.length == 2 && lineList[0].equals(username)){
                    highscore = Integer.parseInt(lineList[1]);
                    break;
                }
            }
        // users is a List<User> of all users. the file consists of username;highscore\n...
        // Go through the file, find the username that is the same as the parameter username.
        } catch (Exception e) {
            return new GameInformation(username, highscore);
        }
        return new GameInformation(username, highscore);
    }

    @Override
    public void save(GameInformation gameInformation) {
        try(Scanner scanner = new Scanner(this.saveFile)){
            //  1. lage en List<String> av alle linjene til filen.
            List<String> lines = new ArrayList<>();
            String line;
            boolean userRegistered = false;
            //  2. sjekke om brukernavnet eksisterer, og i såfall sette gameInformation.getHighscore() til ny highscore om den er større.
            while(scanner.hasNextLine()){
                line = scanner.nextLine();
                String[] lineList = line.split(";");
                if(lineList.length!=2){
                    continue;
                }
                try {
                    Integer.parseInt(lineList[1]);
                } catch (NumberFormatException e) {
                    continue;
                }
                if(gameInformation.getUsername().equals(lineList[0].trim())){
                    userRegistered = true;
                    if(gameInformation.getHighscore()>Integer.parseInt(lineList[1])){
                        line = lineList[0]+";"+gameInformation.getHighscore();
                    }
                }
                lines.add(line);
            }
            if(!userRegistered){
            //  3. Hvis det ikke eksisterer, legge til ny bruker med ny highscore
                lines.add(gameInformation.getUsername()+";"+gameInformation.getHighscore());
            }

            //  4. Gå så gjennom List<String> og skrive til ny fil.

            this.saveFile.getParentFile().mkdirs();
            this.saveFile.createNewFile();
            try(FileWriter writer = new FileWriter(this.saveFile)){
                for(String l : lines){
                    writer.write(l+"\n");
                }
                writer.flush();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
