#2024/8/22
我參考了YT MansCom曼斯康 的影片，模仿製作了自己的第一個Unity小遊戲
https://www.youtube.com/watch?v=KQULD6mnsF0&t=272s

#2024/9/22
添加了平板和手機可以控制的虛擬搖桿，參考 YT BookName 書銘的影片，加上自己編寫在snake.cs下方的虛擬搖桿function。

https://www.youtube.com/watch?v=dP1epSArtBA

 ```
    // 虛擬搖桿控制
    float horizontalInput = fixedJoystick.Horizontal;
    float verticalInput = fixedJoystick.Vertical;

    // 檢查是否有搖桿輸入，並且讓角色沿著搖桿方向移動
    if (horizontalInput != 0 || verticalInput != 0)
    {
        // 搖桿方向更新為 X 軸和 Y 軸的組合
        Vector3 joystickDirection = new Vector3(horizontalInput, verticalInput, 0).normalized;

        // 根據搖桿的輸入來更新角色移動方向
        if (joystickDirection != Vector3.zero)
        {
            direction = joystickDirection;
        } 
```
