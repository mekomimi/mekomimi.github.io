# GitHub 操作指南

## 目录
1. [创建仓库](#创建仓库)
2. [克隆仓库](#克隆仓库)
3. [提交代码](#提交代码)
4. [分支管理](#分支管理)
5. [合并分支](#合并分支)
6. [解决冲突](#解决冲突)
7. [远程仓库操作](#远程仓库操作)

---

## 创建仓库
1. 登录 GitHub。
2. 点击右上角的 `+` 按钮，选择 `New repository`。
3. 填写仓库名称和描述，选择公开或私有。
4. 点击 `Create repository`。

---

## 克隆仓库
```bash
git clone <仓库地址>
```

---

## 提交代码
1. 添加文件到暂存区：
    ```bash
    git add <文件名>
    ```
2. 提交更改：
    ```bash
    git commit -m "提交信息"
    ```
3. 推送到远程仓库：
    ```bash
    git push origin <分支名>
    ```

---

## 分支管理
- 创建分支：
  ```bash
  git branch <分支名>
  ```
- 切换分支：
  ```bash
  git checkout <分支名>
  ```
- 创建并切换分支：
  ```bash
  git checkout -b <分支名>
  ```

---

## 合并分支
1. 切换到目标分支：
    ```bash
    git checkout <目标分支>
    ```
2. 合并分支：
    ```bash
    git merge <被合并分支>
    ```

---

## 解决冲突
1. 打开冲突文件，手动修改冲突部分。
2. 添加修改后的文件到暂存区：
    ```bash
    git add <文件名>
    ```
3. 提交更改：
    ```bash
    git commit -m "解决冲突"
    ```

---

## 远程仓库操作
- 查看远程仓库：
  ```bash
  git remote -v
  ```
- 添加远程仓库：
  ```bash
  git remote add origin <仓库地址>
  ```
- 删除远程仓库：
  ```bash
  git remote remove <远程名>
  ```

---

*本文档适用于 GitHub 的基本操作，适合初学者快速上手。*