# Unity 小遊戲開發記錄

## 2024/8/22
我參考了 [YT MansCom曼斯康 的影片](https://www.youtube.com/watch?v=KQULD6mnsF0&t=272s)，模仿製作了自己的第一個 Unity 小遊戲。影片講解清晰，讓我了解了如何構建簡單的遊戲結構。

---

## 2024/9/22
為了提升遊戲體驗，我為遊戲添加了支援平板和手機的 **虛擬搖桿** 功能，參考了 [YT BookName 書銘的影片](https://www.youtube.com/watch?v=dP1epSArtBA)。  
在影片基礎上，我在 `snake.cs` 的下方新增了控制虛擬搖桿的功能。以下是程式碼片段：

```csharp
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
}
![image](https://github.com/user-attachments/assets/e5ac6c00-cbc7-430e-8824-2698958a4fcf)



