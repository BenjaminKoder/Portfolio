package project.user;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class UserManager implements Serializable{
    private String fileString = "UserInformation.ser";
    private List<User> users;

    public UserManager(){
        this.users = this.readUsers();
    }

    public void writeUsers(){
        // List<User> oldUsers = this.readUsers();
        try {
            FileOutputStream fileOut = new FileOutputStream(fileString);
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(users);
            out.close();
            fileOut.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
    public List<User> readUsers(){
        File file = new File(this.fileString);
        if(!file.exists()||file.length()==0){
            return new ArrayList<>();
        }
        try  {
            ObjectInputStream ois = new ObjectInputStream(new FileInputStream(fileString));
            List<User> list = (List<User>) ois.readObject();
            ois.close();
            return list;
            // Hvis filen med brukere er tom, så må users være lik en ny arraylist, men hvis ikke, så må den bli til den i filen.
        } catch (Exception e) {
            e.printStackTrace();
        }
        // Dersom det skulle vært ett problem i å finne filen:
        return new ArrayList<>();
    }
    public void addUser(User user) {
        if (user==null){
            throw new IllegalArgumentException("Må være en bruker.");
        }
        users.add(user);
        this.writeUsers();
    }
    public String getUserInfo() {
        return this.users.stream().map(u->u.getUsername()+ " "+u.getPassword()).collect(Collectors.joining(", "));
    }
    public List<User> getUsers() {
        return this.users;
    }
    public boolean userHasAccount(User user){
        return this.users.stream()
            .anyMatch(u->u.getUsername().equals(user.getUsername())&&u.getPassword().equals(user.getPassword()));
    }
    public boolean usernameExists(User user){
        return this.users.stream().anyMatch(u->u.getUsername().equals(user.getUsername()));
    }
    public static void main(String[] args) {
        UserManager userManager = new UserManager();
/* 
        // Adding new users
        userManager.addUser(new User("Alice", "password123"));
        userManager.addUser(new User("Bob", "secure456"));
 */
        // Load and display users
        String users = userManager.getUserInfo();
        System.out.println("Users in file: " + users);
    }
}
