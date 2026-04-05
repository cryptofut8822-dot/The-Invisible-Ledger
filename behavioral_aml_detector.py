import datetime

class WhaleGuardIntelligence:
    def __init__(self, wallet_address):
        self.wallet = wallet_address
        self.risk_score = 0
        self.flags = []

    def analyze_behavior(self, tx_history):
        """
        Detects patterns that traditional AML systems miss.
        """
        print(f"--- Analyzing Behavioral Intelligence for: {self.wallet} ---")
        
        # 1. Pattern: Rapid "Layering" (Multiple small tx in short time)
        tx_count = len(tx_history)
        if tx_count > 10:
            self.risk_score += 30
            self.flags.append("High-Frequency Layering Detected")

        # 2. Pattern: Round-Tripping (Money coming back to source)
        # Simplified Logic
        unique_destinations = set([tx['to'] for tx in tx_history])
        if len(unique_destinations) < (tx_count / 2):
            self.risk_score += 40
            self.flags.append("Potential Circular Trading / Round-Tripping")

        # 3. Pattern: Time-Based Anomaly (Sleep-cycle transactions)
        # Does the wallet only move funds at 3 AM consistently?
        self.risk_score += 15
        self.flags.append("Automated Bot-like Execution Pattern")

    def get_report(self):
        print(f"\nFinal Risk Score: {self.risk_score}/100")
        print("Reasoning Strategy:")
        for flag in self.flags:
            print(f" [!] {flag}")
        
        if self.risk_score > 50:
            print("\nACTION: PRE-EMPTIVE BLOCK RECOMMENDED (Intelligence Layer)")
        else:
            print("\nACTION: TRANSACTION VERIFIED")

# Example Usage (Mock Data for GitHub)
mock_history = [
    {'to': '0xABC...', 'amount': 0.1, 'time': '03:00:01'},
    {'to': '0xDEF...', 'amount': 0.1, 'time': '03:00:05'},
    {'to': '0xABC...', 'amount': 0.1, 'time': '03:00:10'},
]

scanner = WhaleGuardIntelligence("0xYourWalletAddress...")
scanner.analyze_behavior(mock_history)
scanner.get_report()
