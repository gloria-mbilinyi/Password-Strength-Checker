
import tkinter as tk
from tkinter import ttk
import re


class PasswordChecker:

    def __init__(self, root):
        self.root = root
        self.root.title("Password Security Checker")
        self.root.geometry("520x590")
        self.root.resizable(False, False)
        self.root.configure(bg="#F4F6FA")

        self.create_interface()

    def create_interface(self):

        # Application heading
        heading = tk.Label(
            self.root,
            text="PASSWORD SECURITY CHECKER",
            font=("Segoe UI", 19, "bold"),
            bg="#F4F6FA",
            fg="#172554"
        )
        heading.pack(pady=(25, 5))

        subtitle = tk.Label(
            self.root,
            text="Evaluate your password security",
            font=("Segoe UI", 10),
            bg="#F4F6FA",
            fg="#64748B"
        )
        subtitle.pack(pady=(0, 25))

        # Password input
        tk.Label(
            self.root,
            text="Enter your password",
            font=("Segoe UI", 11, "bold"),
            bg="#F4F6FA",
            fg="#334155"
        ).pack(anchor="w", padx=45)

        self.password_entry = ttk.Entry(
            self.root,
            font=("Segoe UI", 12),
            show="*",
            width=42
        )
        self.password_entry.pack(padx=45, pady=10, ipady=8)

        # Show password option
        self.show_password = tk.BooleanVar()

        tk.Checkbutton(
            self.root,
            text="Show password",
            variable=self.show_password,
            command=self.toggle_password,
            bg="#F4F6FA",
            fg="#475569",
            activebackground="#F4F6FA"
        ).pack(anchor="w", padx=45)

        # Check button
        tk.Button(
            self.root,
            text="CHECK PASSWORD",
            command=self.check_password,
            bg="#2563EB",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=10
        ).pack(pady=20)

        # Strength result
        tk.Label(
            self.root,
            text="PASSWORD STRENGTH",
            font=("Segoe UI", 10, "bold"),
            bg="#F4F6FA",
            fg="#334155"
        ).pack()

        self.result_label = tk.Label(
            self.root,
            text="Not checked yet",
            font=("Segoe UI", 16, "bold"),
            bg="#F4F6FA",
            fg="#64748B"
        )
        self.result_label.pack(pady=8)

        # Strength progress bar
        self.progress = ttk.Progressbar(
            self.root,
            orient="horizontal",
            length=420,
            mode="determinate",
            maximum=5
        )
        self.progress.pack(pady=8)

        self.score_label = tk.Label(
            self.root,
            text="Security score: 0 / 5",
            font=("Segoe UI", 10),
            bg="#F4F6FA",
            fg="#475569"
        )
        self.score_label.pack(pady=5)

        # Security requirements
        tk.Label(
            self.root,
            text="SECURITY REQUIREMENTS",
            font=("Segoe UI", 10, "bold"),
            bg="#F4F6FA",
            fg="#334155"
        ).pack(pady=(15, 8))

        self.requirements = {}

        checks = [
            ("length", "At least 8 characters"),
            ("uppercase", "Uppercase letter (A-Z)"),
            ("lowercase", "Lowercase letter (a-z)"),
            ("number", "Number (0-9)"),
            ("special", "Special character (!@#$)")
        ]

        for key, description in checks:

            label = tk.Label(
                self.root,
                text=description + "  -",
                font=("Segoe UI", 10),
                bg="#F4F6FA",
                fg="#64748B",
                anchor="w"
            )

            label.pack(anchor="w", padx=55, pady=2)

            self.requirements[key] = label

        # Recommendation
        self.recommendation = tk.Label(
            self.root,
            text="Enter a password to begin.",
            font=("Segoe UI", 9),
            bg="#F4F6FA",
            fg="#64748B",
            wraplength=420
        )
        self.recommendation.pack(pady=15)

        # Clear button
        tk.Button(
            self.root,
            text="CLEAR",
            command=self.clear_fields,
            font=("Segoe UI", 9, "bold"),
            bg="#E2E8F0",
            fg="#334155",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=7
        ).pack()

    def toggle_password(self):

        if self.show_password.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def check_password(self):

        password = self.password_entry.get()

        if not password:
            self.result_label.config(
                text="EMPTY PASSWORD",
                fg="#DC2626"
            )
            self.recommendation.config(
                text="Please enter a password."
            )
            return

        checks = {
            "length": len(password) >= 8,
            "uppercase": bool(re.search(r"[A-Z]", password)),
            "lowercase": bool(re.search(r"[a-z]", password)),
            "number": bool(re.search(r"[0-9]", password)),
            "special": bool(re.search(r"[^A-Za-z0-9]", password))
        }

        score = sum(checks.values())

        for key, passed in checks.items():

            if passed:
                symbol = "✓"
                color = "#15803D"
            else:
                symbol = "✗"
                color = "#DC2626"

            self.requirements[key].config(
                text=self.requirements[key]["text"].split("  ")[0]
                + "  " + symbol,
                fg=color
            )

        self.progress["value"] = score

        self.score_label.config(
            text=f"Security score: {score} / 5"
        )

        if score <= 2:

            strength = "WEAK"
            color = "#DC2626"
            advice = "Use a longer password with mixed characters."

        elif score <= 4:

            strength = "MEDIUM"
            color = "#D97706"
            advice = "Add the missing security requirements."

        else:

            strength = "STRONG"
            color = "#15803D"
            advice = "All five basic security checks passed."

        self.result_label.config(
            text=strength,
            fg=color
        )

        self.recommendation.config(
            text="Recommendation: " + advice,
            fg=color
        )

    def clear_fields(self):

        self.password_entry.delete(0, tk.END)

        self.progress["value"] = 0

        self.result_label.config(
            text="Not checked yet",
            fg="#64748B"
        )

        self.score_label.config(
            text="Security score: 0 / 5"
        )

        self.recommendation.config(
            text="Enter a password to begin.",
            fg="#64748B"
        )

        for key, label in self.requirements.items():

            original_text = {
                "length": "At least 8 characters",
                "uppercase": "Uppercase letter (A-Z)",
                "lowercase": "Lowercase letter (a-z)",
                "number": "Number (0-9)",
                "special": "Special character (!@#$)"
            }

            label.config(
                text=original_text[key] + "  -",
                fg="#64748B"
            )


if __name__ == "__main__":

    root = tk.Tk()

    app = PasswordChecker(root)

    root.mainloop()
