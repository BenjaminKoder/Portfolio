package project.game;

public class GameObject{
    protected double x;
    protected double y;
    private double width;
    private double height;

    public GameObject(double x, double y, double width, double height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        if(width<0){
            this.width = 100;
        }
        if(height<0){
            this.height = 100;
        }
    }
    public double getXPos(){
        return this.x;
    }
    public double getYPos(){
        return this.y;
    }
    public double getWidth(){
        return this.width;
    }
    public double getHeight(){
        return this.height;
    }
    public void setYPos(double y) {
        this.y = y;
    }

}
