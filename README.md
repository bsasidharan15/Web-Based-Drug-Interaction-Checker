# 💊 Web-Based Drug Interaction Checker 🧪

A web-based tool to check interactions between up to five drugs using a preprocessed CSV file of drug interactions. The tool is built with **Gradio** and provides an easy-to-use interface for users to input drug names and get interaction results.

## 🚀 Features

✅ **Fast Lookups**: Preprocesses a CSV file of drug interactions into a dictionary for quick searches.  
✅ **Multi-Drug Support**: Checks interactions between up to five drugs at once.  
✅ **User-Friendly Interface**: Built with Gradio for a simple and intuitive web interface.  
✅ **CSV-Based Data**: Uses a CSV file containing drug interaction data scraped from [Drugs.com](https://www.drugs.com).  
✅ **Efficient Search Algorithm**: Uses sorted drug pairs as dictionary keys to avoid order issues.

## 🛠 How It Works

1. **Scraping Drug Interaction Data**: The drug interaction data was scraped from [Drugs.com](https://www.drugs.com) and stored in a CSV file (`merged_drug_interactions.csv`).
2. **Preprocessing**: The CSV file is loaded and transformed into a dictionary for fast lookups. Each drug pair is stored in a sorted format to ensure consistency (e.g., "Aspirin vs Ibuprofen" is the same as "Ibuprofen vs Aspirin").
3. **Input**: Users enter up to five drug names in the Gradio interface.
4. **Interaction Check**: The tool checks all possible pairs among the entered drugs and retrieves their interaction details from the preprocessed dictionary.
5. **Output**: The results are displayed in an easy-to-read format, including interaction levels and descriptions.

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/drug-interaction-checker.git
   cd drug-interaction-checker
   ```

2. Install the required dependencies:
   ```bash
   pip install gradio pandas
   ```

3. Place your CSV file containing drug interactions in the project directory and update the `CSV_FILE_PATH` variable in `main.py` with the correct path.

## ▶️ Usage

1. Run the `main.py` script:
   ```bash
   python main.py
   ```

2. Open the Gradio interface in your browser (the link will be displayed in the terminal).

3. Enter up to five drug names in the input fields and click **"Check Interactions"**.

4. View the interaction results in the output field.

## 📌 Example

### Input:
- Drug 1: Aspirin  
- Drug 2: Ibuprofen  
- Drug 3: Metformin  
- Drug 4: Paracetamol  
- Drug 5: Amoxicillin  

### Output:
```
Aspirin vs Ibuprofen
Interaction Level: Moderate | Interactions: May increase the risk of gastrointestinal bleeding.

Metformin vs Amoxicillin
Interaction Level: Minor | Interactions: May slightly increase the risk of hypoglycemia.
```

## 📂 Code Structure

### `main.py` Explanation

- **Loading CSV Data**: Reads the `merged_drug_interactions.csv` file and preprocesses it into a dictionary for efficient lookups.
- **Data Processing**: Drug names are normalized (lowercased and stripped of spaces), and drug pairs are stored in a sorted order.
- **Checking Interactions**: When users enter drugs, all possible pairs are checked in the dictionary.
- **Gradio Interface**: The web interface allows users to enter up to five drugs and view interaction results instantly.

### Files & Directories:
- **`main.py`** → The main script containing the Gradio interface and interaction-checking logic.
- **CSV File** → A preprocessed CSV file containing drug interaction data (e.g., `merged_drug_interactions.csv`).

## 📜 Dependencies

- Python 3.7+
- Gradio
- Pandas

## 🤝 Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## 📝 License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.

## 🎖 Acknowledgments

- Thanks to [Drugs.com](https://www.drugs.com) for providing drug interaction data.
- Built with **Gradio** and **Pandas**.
- Inspired by the need for an easy-to-use, web-based drug interaction checker for medical and personal use.
