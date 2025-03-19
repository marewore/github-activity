# GitHub Activity Tracker

## Features
- Fetches and displays recent GitHub events for a user
- Supports event types such as push, pull requests, issues, forks, and more

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/marewore/github-activity.git
    cd github-activity
    ```

2. Create and activate a virtual environment:

    **On Windows:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    **On macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the script, use the following command:

```bash
python github-activity.py <GitHub_Username>
```

Example:

```bash
python github-activity.py marewore
```
