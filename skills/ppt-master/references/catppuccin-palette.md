# Catppuccin 色彩系统参考手册 (Catppuccin Color Palette Reference)

> Catppuccin 是一套专为舒缓视觉疲劳、保持高审美体验而设计的低饱和粉彩（Pastel）主题调色盘生态，提供 4 款风味（Flavors）：1 款明亮浅色（Latte）与 3 款深色（Frappé, Macchiato, Mocha）。

---

## 1. 核心设计原则与在 PPT Master 中的应用规则

1. **层级对比度保证**：
   - 浅色背景（Latte，Base `#EFF1F5`）：主文本使用 `Text`（`#4C4F69`），次要文字使用 `Subtext0`（`#6C6F85`），严禁在浅色底上使用过浅的彩色字。
   - 深色背景（Mocha，Base `#1E1E2E`）：主文本使用 `Text`（`#CDD6F4`），次要文字使用 `Subtext0`（`#A6ADC8`）。
2. **卡片与容器背板层级**：
   - Latte 卡片背景推荐：`Mantle` (`#E6E9EF`) 或纯白 (`#FFFFFF`)，边框使用 `Surface0` (`#CCD0DA`)。
   - Mocha 卡片背景推荐：`Surface0` (`#313244`)，边框使用 `Surface2` (`#585B70`)，代码块/内嵌框使用 `Mantle` (`#181825`)。
3. **语义色（Semantic Role）映射约束**：
   - **品牌主色 (Primary)**：推荐 `Blue` 或 `Lavender`（严谨、科技、现代）
   - **强调色 (Accent)**：推荐 `Mauve` 或 `Sapphire`（高亮、关键指标）
   - **成功/正面 (Positive)**：`Green`（达成、增长、通过）
   - **警告/中性提示 (Warning)**：`Peach` 或 `Yellow`（注意、风险提示）
   - **危险/告警 (Danger)**：`Red` 或 `Maroon`（致命错误、未达标）

---

## 2. 四大风味标准色表 (14 种强调色)

| 颜色名称 | 语义象征 | 🌻 Latte (浅色) | 🪴 Frappé (柔暗) | 🌺 Macchiato (中暗) | 🌿 Mocha (深暗) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Rosewater** | 玫瑰水 | `#DC8A78` | `#F2D5CF` | `#F4DBD6` | `#F5E0DC` |
| **Flamingo** | 火烈鸟粉 | `#DD7878` | `#EEBEBE` | `#F0C6C6` | `#F2CDCD` |
| **Pink** | 浅粉 | `#EA76CB` | `#F4B8E4` | `#F5BDE6` | `#F5C2E7` |
| **Mauve** | 丁香紫 | `#8838EF` | `#CA9EE6` | `#C6A0F6` | `#CBA6F7` |
| **Red** | 珊瑚红 | `#D20F39` | `#E78284` | `#ED8796` | `#F38BA8` |
| **Maroon** | 栗红 | `#E64553` | `#EA999C` | `#EE99A0` | `#EBA0AC` |
| **Peach** | 蜜桃橙 | `#FE640B` | `#EF9F76` | `#F5A97F` | `#FAB387` |
| **Yellow** | 暖杏黄 | `#DF8E1D` | `#E5C890` | `#EED39F` | `#F9E2AF` |
| **Green** | 薄荷绿 | `#40A02B` | `#A6D189` | `#A6DA95` | `#A6E3A1` |
| **Teal** | 蓝绿/青 | `#179299` | `#81C8BE` | `#8BD5CA` | `#94E2D5` |
| **Sky** | 天空蓝 | `#04A5E5` | `#99D1DB` | `#91D7E3` | `#89DCEB` |
| **Sapphire** | 宝石青 | `#209FB5` | `#85C1DC` | `#7DC3E3` | `#74C7EC` |
| **Blue** | 经典蓝 | `#1E66F5` | `#8CAAEE` | `#8AADF3` | `#89B4FA` |
| **Lavender** | 薰衣草淡紫 | `#7287FD` | `#BABBF1` | `#B7BDF8` | `#B4BEFE` |

---

## 3. 中性与层级色表 (Monochrome & Surfaces)

| 层级名称 | 用途说明 | 🌻 Latte | 🪴 Frappé | 🌺 Macchiato | 🌿 Mocha |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Text** | 正文最高对比度文本 | `#4C4F69` | `#C6D0F5` | `#CAD3F5` | `#CDD6F4` |
| **Subtext1** | 次级正文/说明文本 | `#5C5F77` | `#B5BFE2` | `#B8C0E0` | `#BAC2DE` |
| **Subtext0** | 弱对比度说明/图表坐标轴 | `#6C6F85` | `#A5ADCE` | `#A5ADCB` | `#A6ADC8` |
| **Overlay2** | 占位符/禁用状态 | `#7C7F93` | `#949CBB` | `#939AB7` | `#9399B2` |
| **Overlay1** | 强分割线/次级外边框 | `#8C8FA1` | `#838BA7` | `#8087A2` | `#7F849C` |
| **Overlay0** | 细分割线/卡片边框 | `#9CA0B0` | `#737994` | `#6E738D` | `#6C7086` |
| **Surface2** | 悬停/选中状态容器背景 | `#ACB0BE` | `#626880` | `#5B6078` | `#585B70` |
| **Surface1** | 二级卡片/嵌套代码块背景 | `#BCC0CC` | `#51576D` | `#494D64` | `#45475A` |
| **Surface0** | 一级主卡片底板背景 | `#CCD0DA` | `#414559` | `#363A4F` | `#313244` |
| **Base** | 幻灯片主画布背景 | `#EFF1F5` | `#303446` | `#24273A` | `#1E1E2E` |
| **Mantle** | 页眉/页脚/深层底衬 | `#E6E9EF` | `#292C3C` | `#1E2030` | `#181825` |
| **Crust** | 最底层容器背景 | `#DCE0E8` | `#232634` | `#181926` | `#11111B` |
