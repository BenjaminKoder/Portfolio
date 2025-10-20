package project;

import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import project.persistence.GameInformation;
import project.user.User;
import project.user.UserManager;

public class UserManagerTest {
    UserManager userManager;
    @BeforeEach
    public void makeUserTest(){
        this.userManager = new UserManager();
    }
    @Test
    public void addUserTest(){
        User user = new User("Benjamin","Benjaminerkul");
        this.userManager.addUser(user);
        assertTrue(this.userManager.getUsers().contains(user));
    }
    @Test
    public void userExistsTest(){
        User user = new User("Benjamin","Benjaminerkul");
        this.userManager.addUser(user);
        assertTrue(this.userManager.userHasAccount(user));
        assertTrue(this.userManager.usernameExists(user));
    }
}
