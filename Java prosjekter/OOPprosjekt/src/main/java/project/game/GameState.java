package project.game;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Random;


public class GameState {
    private List<GameStateObserver> observers = new ArrayList<>();
    // Liknende UpgradeCenter i cookieclicker; hver gang det skjer endringer på objekter i GameState, så blir handle kjørt i controlleren. GameState styrer alle endringene som skjer med objektene i spillet ved bruk av settere, dvs. endring i posisjon.
    private Player player;
    private int score;
    private int highscore;
    private double vy;
    private double vx;
    private double maxSpeed;
    private double minSpeed;
    private double gravity;
    private double jumpBoost;
    private double xAcceleration;
    private double xDeacceleration;
    private double collideMargin;
    private int screenWidth;
    private int screenHeight;
    private List<GrassPlatform> platforms;
    private Iterator<GrassPlatform> platformIterator;

    private boolean gameOver;
    private boolean playerIsMoving;

    public GameState(Player player){
        if(player==null){
            throw new IllegalArgumentException("Player cannot be null!");
        }
        this.player = player;
        this.gravity = 0.20;
        this.vy = 0;
        this.vx = 0;

        this.maxSpeed = 11;
        this.minSpeed = -maxSpeed;

        this.jumpBoost = 2*maxSpeed;
        this.xAcceleration = 0.4;
        this.xDeacceleration = this.xAcceleration/5;
        this.collideMargin = 20;
        this.platforms = new ArrayList<>();
        this.score = 0;
        this.highscore = 0;

        this.screenWidth = 400;
        this.screenHeight = 600;

        this.gameOver = false;
        this.playerIsMoving = false;
    }
    // Kjører hver gang timeren går av (sies i konstruktøren):
    public void run() {
        
        if (this.platforms.isEmpty()) {
            System.out.println("No platforms exist!");
            return;
        }
        if(this.playerCollidePlatforms()){
            // Endre farten til spilleren til 10, men at akselerasjonen bringer den nedover igjen.
            this.vy-=this.jumpBoost;
            
        }
        this.setVY();
        this.setVX();
        this.setPlayerYPos();
        this.setPlayerXPos();
        this.setPlatformYPos();
        this.setPlatformXPos();
        this.hasPlayerLost();
        this.notifyObservers();
    }
    public void setPlayerIsMoving(boolean playerIsMoving) {
        this.playerIsMoving = playerIsMoving;
    }
    public void setGameOver(boolean gameOver) {
        this.gameOver = gameOver;
    }
    public void clearPlatforms(){
        this.platforms = new ArrayList<>();
    }
    public int getHighscore() {
        return this.highscore;
    }
    public void setHighscore(){
        if(this.score > this.highscore){
            this.highscore = this.score;
        }
    }
    public void setScore(int score) {
        this.score = score;
    }
    public void setVelocity(double vx, double vy){
        this.vx = vx;
        this.vy = vy;
    }
    private void hasPlayerLost(){
        // Sjekker om player har tapt, og i såfall setter gameOver til sant:
        if(this.platforms.stream().allMatch(p->p.getYPos()<-150)){
            this.gameOver=true;
        }
    }
    public boolean isGameOver(){
        return this.gameOver;
    }
    public void loadHighscore(int loadedHighscore){
        if(loadedHighscore>0){
            this.highscore = loadedHighscore;
        }
    }
    private void setPlatformXPos(){
        this.platformIterator = this.platforms.iterator();
        while(this.platformIterator.hasNext()){
            GrassPlatform p = this.platformIterator.next();
            if(p.getCrackedPlatform()){
                if(p.getXPos()+p.getWidth()-10>=screenWidth+150){
                    p.setPlatformVX(-1);
                }else if(p.getXPos()+10<=-150){
                    p.setPlatformVX(1);
                }
                if(p.getPlatformVX()>0){
                    p.setXPos(p.getXPos()+p.getPlatformVX()+this.score/25);
                    // System.out.println(p.getPlatformVX()+this.score/25);
                }
                if(p.getPlatformVX()<0){
                    p.setXPos(p.getXPos()+p.getPlatformVX()-this.score/25);
                    // System.out.println(p.getPlatformVX()-this.score/25);
                }
            }
        }
    }
    private void setPlatformYPos(){
        int platformsToAdd = 0;
        this.platformIterator = this.platforms.iterator();
        while(this.platformIterator.hasNext()){
            GameObject p = this.platformIterator.next();
            p.setYPos(p.getYPos()-this.vy);
            if(p.getYPos()>this.screenHeight){ 
                this.platformIterator.remove();
                this.score++;
                platformsToAdd++;
            }
        }
        if(platformsToAdd>0){
            this.generateRandomPlatforms(platformsToAdd);
        }
    }
    private void setPlayerXPos(){
        if(this.player.getXPos()+this.vx>this.screenWidth){
            this.player.setXPos(0-this.player.getWidth());
        }
        else if(this.player.getXPos()+this.vx+this.player.getWidth()<0){
            this.player.setXPos(this.screenWidth);
        }
        else{
            this.player.setXPos(this.player.getXPos()+this.vx);
        }
    }
    private void setPlayerYPos(){
        double newPlayerYPos = this.player.getYPos() + 0.1 * this.vy;
        if (newPlayerYPos > 400) {
            newPlayerYPos = 400;
        } else if (newPlayerYPos < 200) {
            newPlayerYPos = 200;
        }

        this.player.setYPos(newPlayerYPos);
    }
    private void setVY(){
        this.vy +=this.gravity;
        if(this.vy>this.maxSpeed){
            this.vy = this.maxSpeed;
        }else if(this.vy<this.minSpeed){
            this.vy = this.minSpeed;
        }
    }
    private void setVX(){
        if(this.vx>this.maxSpeed){
            this.vx = this.maxSpeed;
        } else if(this.vx<this.minSpeed){
            this.vx = this.minSpeed;
        }
        if(!this.playerIsMoving && this.vx>0){
            this.vx-=this.xDeacceleration;
        }else if(!this.playerIsMoving && this.vx<0){
            this.vx+=this.xDeacceleration;
        }
        // Margin:
        if(!this.playerIsMoving && Math.abs(this.vx)<0.1){
            this.vx = 0;
        }
    }
    public void movePlayerLeft() {
        this.vx-=this.xAcceleration;
        this.playerIsMoving = true;
    }
    public void movePlayerRight() {
        this.vx+=this.xAcceleration;
        this.playerIsMoving = true;
    }
    public void generateRandomPlatforms(int maxNumberOfPlatforms){
        Random random = new Random();
        double nextPlatformY = -650;
        double platformSpacing = 250;
        double screenWidth = this.screenWidth;
        int crackedPlatformInt;
        boolean crackedPlatform = false;
        for(int i = 0;i<maxNumberOfPlatforms;i++){
            double x = random.nextDouble() * (screenWidth+100);
            // 1 av 10 platformer blir cracked:
            crackedPlatformInt = random.nextInt(10);
            if(crackedPlatformInt==0){
                crackedPlatform = true;
            }
            GrassPlatform grassPlatform = new GrassPlatform(x-150, nextPlatformY, crackedPlatform);
            if(i==4){
                grassPlatform = new GrassPlatform(100, nextPlatformY, crackedPlatform);
            }
            this.platforms.add(grassPlatform);
            nextPlatformY+=platformSpacing;
        }
    }
    public List<GrassPlatform> getPlatforms(){
        return this.platforms;
    }
    public boolean playerCollidePlatforms(){
        this.platformIterator = this.platforms.iterator();
        while(this.platformIterator.hasNext()){
            GrassPlatform p = this.platformIterator.next();
            if(this.vy > 0 && this.player.getXPos()<=p.getXPos()+p.getWidth()-this.player.getWidth() && 
            this.player.getXPos()+this.player.getWidth()>=p.getXPos()+20 && 
            this.player.getYPos()+this.player.getHeight()-35>=p.getYPos()&& 
            this.player.getYPos()+this.player.getHeight()-this.collideMargin-35<=p.getYPos()){
                if(p.getCrackedPlatform()){
                    this.score++;
                    p.setYPos(p.getYPos()-1250);
                    Random random = new Random();
                    double x = random.nextDouble() * (screenWidth+100);
                    p.setXPos(x-150);
                }
                return true;
            } 
        }
        return false;
    }
    public void addListener(GameStateObserver listener) {
        if(listener==null){
            throw new IllegalArgumentException("Listener is null");
        }
        this.observers.add(listener);
    }
    public void notifyObservers() {
        for(GameStateObserver observer : observers){
            observer.handle();
        }
    }
    public int getScore() {
        return this.score;
    }
}
