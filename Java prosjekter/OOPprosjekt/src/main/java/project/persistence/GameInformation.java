package project.persistence;

public class GameInformation {

    private String username;
    private int highscore;

    public GameInformation(String username, int highscore){
        if(username==null||username.isEmpty()){throw new IllegalArgumentException("Username cannot be empty");}
        if(highscore<0){throw new IllegalArgumentException("Highscore cannot be negative");}
        this.username = username.trim();
        this.highscore = highscore;
    }
    public String getUsername() {
        return this.username;
    }
    public int getHighscore() {
        return this.highscore;
    }
}
