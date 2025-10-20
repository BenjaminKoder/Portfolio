package project.user;

import java.io.Serializable;

public class User implements Serializable{
    private String username;
    private String password;
    public User(String username, String password){
        this.username = username;
        this.password = password;
    }
    public String getUsername() {
        return this.username;
    }
    public String getPassword() {
        return this.password;
    }

    /* public static void main(String[] args){
        try {
            User user = new User();
            user.username = "Bro";
            user.password = "Code";
            FileOutputStream fileOut = new FileOutputStream("UserInformation.ser");
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(user);
            out.close();
            fileOut.close();   
            // System.out.println("Saving file to: " + new java.io.File("UserInformation.ser").getAbsolutePath());
        } catch (Exception e) {
            e.printStackTrace();
        }
    } */
}
