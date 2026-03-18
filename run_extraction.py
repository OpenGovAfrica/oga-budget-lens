from oga_budget_lens.text_extraction import extract_text_pipeline, save_extraction_output
pdf = "data/samples/kenya_budget_2023_24.pdf"
result = extract_text_pipeline(pdf)
save_extraction_output(result, pdf)
print("Extraction complete")