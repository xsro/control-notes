# 滑模控制学习笔记（LaTeX）

## 编译方法

- 使用 xelatex：`xelatex main.tex` → `biber main` → `xelatex main.tex` → `xelatex main.tex`
- 使用 tectonic：`tectonic main.tex`
- 只编译某一章：打开 `main.tex` 中的 `\includeonly{body/nonlinear}`（按需修改文件名）

## 目录结构

```
main.tex                  文档入口：宏包、定理环境、\part 与各章 \include
main_biber.bib            参考文献（由 Zotero/tex2ast 导出，APA 样式）

body/
  pre.tex                 第1章 前言：动机、阅读路线、符号与连续性回顾的入口
  pre_notation.tex        §1.3 符号约定、分数幂奇函数、Young/Gronwall 不等式
  pre_continuous.tex      §1.4 连续性谱系、四种解概念总表
  nonlinear.tex           第2章 非线性系统：右端 Lipschitz 连续（经典解）
  bounded.tex             第3章 非光滑控制系统：右端有界（Carathéodory/Filippov/Dini/Clarke）
  motivation.tex          第4章 案例：一阶 bang-bang、Utkin 等效控制 vs. Filippov
  sta.tex                 第5章 经典 STA 算法（草稿，已编入正文）
  sta_basic.tex           STA 基本算法
  sta_stability.tex       STA 稳定性与增益条件

asserts/                  图片与 TikZ 源文件
simulation/               仿真脚本与输出图
```

## 章节逻辑

全书按“右端正则性由强到弱”组织：

1. **数学准备**：连续 / 一致连续 / 绝对连续 / Lipschitz 连续的关系，以及三种解概念总表；
2. **Lipschitz 连续**：局部/全局存在唯一性、有限逃逸时间、连续依赖、比较原理与有限时间到达估计；
3. **右端有界**：Carathéodory 解、Filippov 解、sample-and-hold 解，以及 Dini 导数、Clarke 广义梯度、集值 Lie 导数和非光滑 LaSalle；
4. **案例**：用 $\dot x=-\operatorname{sgn}(x)+\delta$ 串起上述概念，辨析 Utkin 等效控制的适用边界。

## 约定

- 定理类环境（定理/引理/命题/推论/定义/例/算法/注）按章编号、共用一个计数器；
- 引用采用 biblatex `numeric` 样式（按首次引用顺序编号），正文中形如 `[3]`、`[3, Theorem 3.1]`；
- 教材引用约定：`khalilNonlinearSystems` 指 *Nonlinear Systems* (3rd ed., 2002)，`khalilNonlinearControl2015` 指 *Nonlinear Control* (2015)；
- 第 5 章 STA 已编入正文，但仍是草稿（参数条件与符号约定待核对，见章末 TODO）。
