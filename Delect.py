import tkinter as tk
from tkinter import messagebox, Button, Listbox, Scrollbar, VERTICAL, simpledialog, END, Frame, Checkbutton, IntVar
import requests

# 获取仓库列表
def get_repos(access_token):
    api_url = "https://api.github.com/user/repos?per_page=100&type=owner"
    headers = {"Authorization": f"token {access_token}", "Accept": "application/vnd.github.v3+json"}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return [repo['full_name'] for repo in response.json()]
    else:
        messagebox.showerror("错误", f"获取仓库列表失败：{response.json().get('message', '未知错误')}")
        return []

# 保存Access Token到文件
def save_access_token(file_path, token):
    with open(file_path, 'w') as file:
        file.write(token)

# 从文件获取Access Token
def get_access_token(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        token = simpledialog.askstring("输入", "请输入您的GitHub Access Token：")
        if token:
            save_access_token(file_path, token)
            return token
        else:
            messagebox.showwarning("警告", "未输入Access Token。")
            return None

# 删除指定仓库
def delete_repo(access_token, repo_full_name):
    api_url = f"https://api.github.com/repos/{repo_full_name}"
    headers = {"Authorization": f"token {access_token}", "Accept": "application/vnd.github.v3+json"}
    response = requests.delete(api_url, headers=headers)
    if response.status_code == 204:
        return True
    else:
        messagebox.showerror("删除失败", f"删除仓库失败：{response.json().get('message', '未知错误')}")
        return False

def main():
    root = tk.Tk()
    root.title("GitHub仓库删除工具")

    frame = Frame(root)
    frame.pack(padx=10, pady=10)

    scrollbar = Scrollbar(frame, orient=VERTICAL)
    listbox = Listbox(frame, selectmode=tk.EXTENDED, yscrollcommand=scrollbar.set, height=10, width=50)
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    select_all_var = IntVar()
    select_all_cb = Checkbutton(root, text="全选/全不选", variable=select_all_var, command=lambda: select_all())
    select_all_cb.pack(pady=5)

    get_repos_button = Button(root, text="获取我的仓库", command=lambda: on_get_repos())
    get_repos_button.pack(pady=5)

    delete_selected_button = Button(root, text="删除选中的仓库", command=lambda: on_delete_selected())
    delete_selected_button.pack(pady=5)

    def select_all():
        if select_all_var.get() == 1:
            listbox.select_set(0, END)
        else:
            listbox.select_clear(0, END)

    def on_get_repos():
        access_token = get_access_token("github_token.txt")
        if access_token:
            repos = get_repos(access_token)
            listbox.delete(0, END)
            for repo in repos:
                listbox.insert(END, repo)

    def on_delete_selected():
        selected_indices = listbox.curselection()
        if not selected_indices:
            messagebox.showinfo("提示", "请选择至少一个仓库进行删除")
            return
        access_token = get_access_token("github_token.txt")
        if access_token:
            for i in selected_indices[::-1]:  # 从后向前删除，避免索引变化影响结果
                repo_full_name = listbox.get(i)
                if delete_repo(access_token, repo_full_name):
                    listbox.delete(i)

    root.mainloop()

if __name__ == "__main__":
    main()
