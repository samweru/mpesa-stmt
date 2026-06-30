import argparse
import pandas as pd

def merge_xlsx_sheets(file_path, skip_indices, drop_first_col):
    """
    Reads an Excel file, skips specified sheet indices, 
    optionally drops the first column, and merges the rest.
    """
    # 1. Read all sheets into memory
    all_sheets = pd.read_excel(file_path, sheet_name=None)
    sheet_names = list(all_sheets.keys())
    
    # 2. Filter and process sheets
    sheets_to_merge = []
    for idx, name in enumerate(sheet_names):
        if idx not in skip_indices:
            df = all_sheets[name]
            
            # Drop the first column if the flag is enabled and data exists
            if drop_first_col and not df.empty and len(df.columns) > 0:
                df = df.iloc[:, 1:]
                
            sheets_to_merge.append(df)
            
    if not sheets_to_merge:
        print("Error: No sheets left to merge after exclusions.")
        return

    # 3. Combine remaining structures
    combined_data = pd.concat(sheets_to_merge, ignore_index=True)
    
    # 4. Write back to the target workbook file
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        combined_data.to_excel(writer, sheet_name='Merged_Master', index=False)
    print(f"Success: Merged target sheets into 'Merged_Master'.")
    print(f"  - Skipped indices: {skip_indices}")
    print(f"  - Removed first column: {drop_first_col}")

if __name__ == "__main__":
    # Set up CLI argument rules
    parser = argparse.ArgumentParser(description="Merge Excel sheets by omitting chosen indices/columns.")
    
    # Required positional argument
    parser.add_argument("file_path", type=str, help="Absolute path to your target .xlsx file")
    
    # Optional skip flag
    parser.add_argument(
        "--skip", 
        type=int, 
        nargs="*", 
        default=[0, 1], 
        help="Space-separated list of zero-based sheet indices to skip (Default: 0 1)"
    )
    
    # Optional drop column flag
    parser.add_argument(
        "--drop-first-col",
        action="store_true",
        help="Pass this flag to delete the first column from all processed sheets before merging"
    )
    
    # Parse parameters from terminal interface call
    args = parser.parse_args()
    
    # Run the controller
    merge_xlsx_sheets(args.file_path, args.skip, args.drop_first_col)
