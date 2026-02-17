# Project 1-The Game of Hog

>When students in the past have tried to implement the functions without thoroughly reading the problem description, they’ve often run into issues. 😱 **Read each description thoroughly before starting to code.**

这主要是一个二人的零和博弈游戏，深究应该会涉及到博弈论相关的知识

大约需要4h

## Rule

主要规则如下：

- **Sow Sad**. If any of the dice outcomes is a 1, the current player's score for the turn is `1`.

In a normal game of Hog, Sow Sad is all the rules. To spice up the game, we'll include some special rules:


- **Boar Brawl**. A player who rolls zero dice scores three times the absolute difference between the tens digit of the opponent’s score and the ones digit of the current player’s score, or 1, whichever is higher. The ones digit refers to the rightmost digit and the tens digit refers to the second-rightmost digit. If a player's score is a single digit (less than 10), the tens digit of that player's score is 0.

可以选择不掷色子获得自身个位数与对方十位数差的绝对值的三倍的分数(最小为1)


- **Sus Fuss**. We call a number [_sus_](https://en.wikipedia.org/wiki/Sus_%28genus%29) if it has exactly 3 or 4 factors, including 1 and the number itself. If, after rolling, the current player's score is a sus number, they gain enough points such that their score instantly increases to the next prime number.

掷色子后的分数如果恰好有三个或四个因数(包括1和本身)，那么自动将分数提高到下一个质数

## Begin

>For the project, you'll only be making changes to `hog.py`.



## Phase 1: Rules of the Game

>In the first phase, you will develop a simulator for the game of Hog.

值得注意的是每个Problem在正式进行代码书写前，都有一个增进理解的What printed？的项目，主要是有一个对问题的划分意识

### Problem 0 (0 pt)

增进理解

### Problem 1 (2 pt)

完成对于sow_sad的判断，单个回合掷色子得到的分数计算

### Problem 2 (2 pt)

完成Boar-Brawl的实现，计算不抛掷色子情况下的得分判断

### Problem 3 (2 pt)

题面可能说的不太清楚，输入的是三个参数，综合前两个函数即可

### Problem 4 (2 pt)

这是为了sus规则的函数，到这里实现了所有的规则

### Problem 5 (4 pt)

实现最核心的play函数

## Interlude: User Interfaces


>There are no required problems in this section of the project, just some examples for you to read and understand. See Phase 2 for the remaining project problems.


感觉是给出了项目重构的一些思路和方法，如何在原有简单代码的基础上比较好的扩展和方便改进


## Phase 2: Strategies

>In this phase, you will experiment with ways to improve upon the basic strategy of always rolling five dice. A _strategy_ is a function that takes two arguments: the current player's score and their opponent's score. It returns the number of dice the player will roll, which can be from 0 to 10 (inclusive).


### Problem 6 (2 pt)

直接lambda实现就好了

### Problem 7 (2 pt)

写个循环嵌套暴力遍历得了


### Problem 8 (2 pt)

>**Important:** To implement this function, you will need to use a new piece of Python syntax. We would like to write a function that accepts an arbitrary number of arguments, and then calls another function using exactly those arguments. Here's how it works.


只需要使用例子中的`*args`即可

### Problem 9 (2 pt)

下面是一个有问题的代码，笔者想了很久，发现在比较时会调用roll_dice函数，而判断后赋值调用第二次，这就会导致结果受到影响

```Python
num = 1  
roll_num = 1  
make_averaged_func = make_averaged(roll_dice, samples_count)  
max_average = 0  
while num <= 10:  
    if make_averaged_func(num, dice) > max_average:  
        max_average = make_averaged_func(num, dice)  
        roll_num = num  
    num += 1  
return roll_num
```

可以增加一个临时的局部变量进行控制，下面是正确的代码：

```Python
num = 1  
roll_num = 1  
make_averaged_func = make_averaged(roll_dice, samples_count)  
max_average = 0  
while num <= 10:  
    average_container = make_averaged_func(num, dice)  
    if average_container > max_average:  
        max_average = average_container  
        roll_num = num  
    num += 1  
return roll_num
```


### Running Experiments


还有一个模拟胜率的模块，真是相当完善的评测机制


### Problem 10 (2 pt)

简单的选择结构

### Problem 11 (2 pt)


同理可得

### Optional: Problem 12 (0 pt)

因为没有给出色子的参数，所以如果要测试会比较麻烦，干脆给出一个比较简单的策略

```Python
return 0 if sus_update(0, score, opponent_score) >= GOAL else 6
```



在绝对的运气面前策略似乎不太有效呢(欧皇发言doge)

![hog](https://cdn.jsdelivr.net/gh/Eurekaimer/MyIMGs@main/img/hog)