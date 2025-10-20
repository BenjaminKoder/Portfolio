package project.game;

public class Player extends GameObject{
    public Player(double x, double y, double width, double height){
        super(x,y,width,height);
        
    }
    public void setXPos(double x){
        super.x=x;
    }
    
}
