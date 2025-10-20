```mermaid
---
title: Class Diagram JumpyJump game
---
classDiagram
    class GameState {
        - List<GameStateObserver> observers
        - Player player
        - int score
        - int highscore
        - double vy
        - double vx
        - double maxSpeed
        - double minSpeed
        - double gravity
        - double jumpBoost
        - double xAcceleration
        - double xDeacceleration
        - double collideMargin
        - int screenWidth
        - int screenHeight
        - List<GameObject> platforms
        - Iterator<GameObject> platformIterator
        - boolean gameOver
        - boolean playerIsMoving
        + GameState(Player player)
        + void run()
        + void setPlayerIsMoving(boolean playerIsMoving)
        + void setGameOver(boolean gameOver)
        + void clearPlatforms()
        + int getHighscore()
        + void setHighscore()
        + void setScore(int score)
        + void setVelocity(double vx, double vy)
        + boolean isGameOver()
        + void loadHighscore(int loadedHighscore)
        + void movePlayerLeft()
        + void movePlayerRight()
        + void generateRandomPlatforms(int maxNumberOfPlatforms)
        + List<GameObject> getPlatforms()
        + boolean playerCollidePlatforms()
        + void addListener(GameStateObserver listener)
        + void notifyObservers()
        + int getScore()
    }

    class GameObject {
        - double x
        - double y
        - double width
        - double height
        + GameObject(double x, double y, double width, double height)
        + double getXPos()
        + double getYPos()
        + double getWidth()
        + double getHeight()
        + void setYPos(double y)
    }
    
    class Player {
        + Player(double x, double y, double width, double height)
    }
    class GameStateObserver {
        <<interface>>
        + handle()
    }
    
    GameObject <|-- Player
    GameState "1" -- "n" GameStateObserver : observers
    GameState "1" -- "1" Player : player
    GameState "1" -- "n" GameObject : platforms