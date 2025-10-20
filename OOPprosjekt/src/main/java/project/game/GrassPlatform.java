package project.game;

import java.util.Random;

public class GrassPlatform extends GameObject{
    private boolean crackedPlatform;
    private double platformVX;

    public GrassPlatform(double x, double y, boolean crackedPlatform){
        super(x,y,200,150);
        this.crackedPlatform = crackedPlatform;
        Random random = new Random();
        int randomInt = random.nextInt(2);
        this.platformVX = randomInt;
        if(this.platformVX==0){
            this.platformVX = -1;
        } 
    }
    public boolean getCrackedPlatform(){
        return this.crackedPlatform;
    }
    public void setXPos(double x){
        this.x = x;
    }
    public void setPlatformVX(double platformVX){
        this.platformVX = platformVX;
    }
    public double getPlatformVX() {
        return this.platformVX;
    }
}
