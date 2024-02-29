# GitHub Repository Manager

This Python GUI application allows users to manage their GitHub repositories with ease. It provides functionalities to list your GitHub repositories, select multiple repositories for batch operations, and delete them directly from the interface.

## Features

- **List Repositories**: Fetch and display a list of all your GitHub repositories.
- **Batch Select**: Select multiple repositories at once for batch operations.
- **Delete Repositories**: Delete selected repositories directly from the application.
- **Access Token Management**: Securely request and store your GitHub access token for API requests.
- **Error Handling**: Display error messages for failed API requests or incorrect inputs.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install the `requests` library using pip:

    ```bash
    pip install requests
    ```

3. Download the script or clone the repository to your local machine.

## Usage

1. Run the script using Python:

    ```bash
    python github_repo_manager.py
    ```

2. Upon first launch, the application will prompt you to enter your GitHub Access Token. This token is necessary for the application to interact with the GitHub API on your behalf. You can generate an access token from your GitHub account settings under "Developer settings" > "Personal access tokens".

3. Once the token is provided, use the "获取我的仓库" (Get My Repositories) button to list all your repositories.

4. Use the list box to select the repositories you want to delete. You can select multiple repositories by holding down the `Ctrl` key while clicking.

5. After selecting, click the "删除选中的仓库" (Delete Selected Repositories) button to delete them. The application will ask for confirmation before proceeding with the deletion.

6. The "全选/全不选" (Select All/Deselect All) checkbox allows you to quickly select or deselect all listed repositories.

## Important Notes

- The application uses your GitHub Access Token to authenticate API requests. This token is stored locally and should be kept secure.
- Deleting a repository is irreversible. Please use the delete feature with caution.

## License

This project is open-source and available under the MIT License.

## Contributing

Contributions to the GitHub Repository Manager are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

## Contact

If you encounter any issues or have suggestions for improvements, please open an issue in the GitHub repository.

---

This README provides a basic overview of the application's functionality, installation process, and usage. You can customize it further based on the specifics of your project and any additional features you might add in the future.
