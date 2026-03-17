class TableDetector:
    def __init__(self, y_threshold=10):
        self.y_threshold = y_threshold

    def get_y_center(self, token):
        return (token["y0"] + token["y1"]) / 2

    def group_rows(self, tokens):
        tokens = sorted(tokens, key=lambda t: self.get_y_center(t))
        rows = []
        current_row = []

        for token in tokens:
            if not current_row:
                current_row.append(token)
                continue

            if abs(
                self.get_y_center(token) -
                self.get_y_center(current_row[-1])
            ) <= self.y_threshold:
                current_row.append(token)
            else:
                rows.append(current_row)
                current_row = [token]

        if current_row:
            rows.append(current_row)

        return rows

    def sort_row(self, row):
        return sorted(row, key=lambda t: t["x0"])

    def build_table(self, rows):
        table = []
        for row in rows:
            sorted_row = self.sort_row(row)
            table.append([t["text"] for t in sorted_row])
        return table

    def has_column_alignment(self, rows):
        if len(rows) < 3:
            return False

        sample = rows[:3]
        x_positions = [[t["x0"] for t in row] for row in sample]

        for col_idx in range(min(len(r) for r in sample)):
            col_vals = [row[col_idx] for row in x_positions]
            if max(col_vals) - min(col_vals) > 50:
                return False

        return True

    def detect(self, page_data):
        tokens = page_data["tokens"]

        if not tokens:
            return {
                "page_number": page_data["page_number"],
                "tables": []
            }

        rows = self.group_rows(tokens)

        if len(rows) < 3:
            return {
                "page_number": page_data["page_number"],
                "tables": []
            }

        if not self.has_column_alignment(rows):
            return {
                "page_number": page_data["page_number"],
                "tables": []
            }

        table = self.build_table(rows)

        avg_cols = sum(len(r) for r in table) / len(table)

        inconsistent_rows = sum(
            1 for r in table if abs(len(r) - avg_cols) > 2
        )

        if inconsistent_rows > len(table) * 0.5:
            return {
                "page_number": page_data["page_number"],
                "tables": []
            }

        # 🔥 FILTER 3
        long_rows = sum(1 for r in table if len(r) > 8)

        if long_rows > len(table) * 0.5:
            return {
                "page_number": page_data["page_number"],
                "tables": []
            }

        # FINAL RETURN
        return {
            "page_number": page_data["page_number"],
            "tables": [
                {
                    "rows": table
                }
            ]
        }