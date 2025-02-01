import gradio as gr
import pandas as pd

# Load the CSV containing drug interactions once, for better performance
CSV_FILE_PATH = 'merged_drug_interactions.csv'  # Update this path to your CSV file

# Function to preprocess the CSV into a dictionary for fast lookups
def preprocess_csv():
    df = pd.read_csv(CSV_FILE_PATH)
    interaction_dict = {}
    
    # Loop through each row in the dataframe to populate the dictionary
    for _, row in df.iterrows():
        drug1 = row['Drug 1 Name'].strip().lower()
        drug2 = row['Drug 2 Name'].strip().lower()
        interaction_level = row['Interaction Level']
        interaction_description = row['Interaction']
        
        # Sort the drugs to avoid order issues (Aspirin vs Ibuprofen = Ibuprofen vs Aspirin)
        pair = tuple(sorted([drug1, drug2]))
        
        # Store the interaction in the dictionary
        interaction_dict[pair] = (interaction_level, interaction_description)
    
    return interaction_dict

# Preprocess the CSV into a dictionary (done only once)
interaction_dict = preprocess_csv()

# Function to check interactions for multiple drugs
def check_interactions_from_csv(drug1, drug2, drug3, drug4, drug5):
    # Gather all drug inputs into a list and normalize them (lowercase and strip)
    drug_list = [drug1.strip().lower(), drug2.strip().lower(), drug3.strip().lower(), drug4.strip().lower(), drug5.strip().lower()]
    
    interactions = []
    
    # Form pairs of drugs and search in the dictionary
    for i in range(len(drug_list)):
        for j in range(i + 1, len(drug_list)):
            drug_pair = tuple(sorted([drug_list[i], drug_list[j]]))  # Sort to handle interchangeable drugs
            
            # Check if the pair exists in the dictionary
            if drug_pair in interaction_dict:
                interaction_level, interaction_description = interaction_dict[drug_pair]
                interactions.append({
                    'drug1': drug_list[i].capitalize(),
                    'drug2': drug_list[j].capitalize(),
                    'interaction_level': interaction_level,
                    'interaction': interaction_description
                })

    if not interactions:
        return "No known interactions for the given drugs."
    
    # Return the interactions as a formatted string
    result_str = ""
    for interaction in interactions:
        result_str += f"{interaction['drug1']} vs {interaction['drug2']}\n" \
                      f"Interaction Level: {interaction['interaction_level']} | Interactions: {interaction['interaction']}\n\n"
    
    return result_str

# Gradio interface using Blocks API
with gr.Blocks() as demo:
    gr.Markdown("# Drug Interaction Checker from CSV")
    
    # Input for five drugs
    drug_input1 = gr.Textbox(label="Drug 1", placeholder="e.g., Aspirin")
    drug_input2 = gr.Textbox(label="Drug 2", placeholder="e.g., Ibuprofen")
    drug_input3 = gr.Textbox(label="Drug 3", placeholder="e.g., Metformin")
    drug_input4 = gr.Textbox(label="Drug 4", placeholder="e.g., Paracetamol")
    drug_input5 = gr.Textbox(label="Drug 5", placeholder="e.g., Amoxicillin")
    
    # Output field for interaction results
    output = gr.Textbox(label="Interaction Results", interactive=False, lines=10)
    
    # Define button click action
    btn = gr.Button("Check Interactions")
    
    # Define button click action
    btn.click(fn=check_interactions_from_csv, 
              inputs=[drug_input1, drug_input2, drug_input3, drug_input4, drug_input5], 
              outputs=output)

# Launch the Gradio interface
if __name__ == "__main__":
    demo.launch()
