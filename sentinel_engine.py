import hashlib
import time

class SentinelChainEngine:
    """
    Advanced Intelligence Layer for Web3 Transaction Monitoring.
    Focus: Detecting non-linear movement patterns.
    """
    def __init__(self):
        self.anomaly_threshold = 0.75
        self.intelligence_db = {}

    def calculate_velocity(self, tx_list):
        """
        Calculates Asset Velocity: How fast money moves through a wallet.
        High velocity + Low holding time = Potential wash trading or layering.
        """
        if not tx_list: return 0
        
        timestamps = [tx['timestamp'] for tx in tx_list]
        timespan = max(timestamps) - min(timestamps)
        
        # Velocity = Transactions / Time
        velocity = len(tx_list) / (timespan if timespan > 0 else 1)
        return velocity

    def detect_entropy(self, wallet_address, target_addresses):
        """
        Address Entropy: Checks if a wallet is interacting with 
        high-risk clusters or diverse unidentified smart contracts.
        """
        unique_targets = len(set(target_addresses))
        total_tx = len(target_addresses)
        
        # Entropy ratio: High entropy means scattered, suspicious movement.
        entropy_ratio = unique_targets / total_tx if total_tx > 0 else 0
        return round(entropy_ratio, 4)

    def run_diagnostic(self, wallet, history):
        velocity = self.calculate_velocity(history)
        entropy = self.detect_entropy(wallet, [tx['to'] for tx in history])
        
        print(f"[*] Diagnostic for {wallet[:10]}...")
        print(f" |-> Asset Velocity: {velocity:.4f} tx/sec")
        print(f" |-> Address Entropy: {entropy}")
        
        if velocity > 5.0 and entropy > 0.8:
            return "SIGNAL: HIGH-RISK BEHAVIORAL ANOMALY"
        return "SIGNAL: STABLE TRANSACTION PATTERN"

# --- Developer Testing Block ---
if __name__ == "__main__":
    # Mock Data: Real developers use Unix timestamps and Hex addresses
    mock_tx_data = [
        {'to': '0x71C...', 'timestamp': 1712230000},
        {'to': '0x82D...', 'timestamp': 1712230005},
        {'to': '0x93E...', 'timestamp': 1712230010},
        {'to': '0x71C...', 'timestamp': 1712230015},
    ]
    
    engine = SentinelChainEngine()
    result = engine.run_diagnostic("0xYourDeveloperWalletAddress", mock_tx_data)
    print(f"\n[FINAL REPORT] {result}")
