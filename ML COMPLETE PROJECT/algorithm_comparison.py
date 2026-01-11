import matplotlib.pyplot as plt
import numpy as np

# Algorithm statistics
algorithms = ['Apriori', 'FP-Growth']
total_rules = [388, 388]
avg_support = [0.0297, 0.0297]
avg_confidence = [0.2311, 0.2311]
avg_lift = [1.0475, 1.0475]

# Create comparison chart
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))

# Total Rules
ax1.bar(algorithms, total_rules, color=['skyblue', 'lightcoral'])
ax1.set_title('Total Rules Generated')
ax1.set_ylabel('Number of Rules')
for i, v in enumerate(total_rules):
    ax1.text(i, v + 5, str(v), ha='center')

# Average Support
ax2.bar(algorithms, avg_support, color=['lightgreen', 'gold'])
ax2.set_title('Average Support')
ax2.set_ylabel('Support Value')
for i, v in enumerate(avg_support):
    ax2.text(i, v + 0.001, f'{v:.4f}', ha='center')

# Average Confidence
ax3.bar(algorithms, avg_confidence, color=['plum', 'orange'])
ax3.set_title('Average Confidence')
ax3.set_ylabel('Confidence Value')
for i, v in enumerate(avg_confidence):
    ax3.text(i, v + 0.01, f'{v:.4f}', ha='center')

# Average Lift
ax4.bar(algorithms, avg_lift, color=['lightblue', 'pink'])
ax4.set_title('Average Lift')
ax4.set_ylabel('Lift Value')
for i, v in enumerate(avg_lift):
    ax4.text(i, v + 0.01, f'{v:.4f}', ha='center')

plt.tight_layout()
plt.suptitle('Apriori vs FP-Growth Algorithm Comparison', y=1.02, fontsize=14, fontweight='bold')
plt.show()

# Summary table
print("\nAlgorithm Performance Summary:")
print("=" * 50)
print(f"{'Metric':<15} {'Apriori':<12} {'FP-Growth':<12}")
print("-" * 50)
print(f"{'Total Rules':<15} {total_rules[0]:<12} {total_rules[1]:<12}")
print(f"{'Avg Support':<15} {avg_support[0]:<12.4f} {avg_support[1]:<12.4f}")
print(f"{'Avg Confidence':<15} {avg_confidence[0]:<12.4f} {avg_confidence[1]:<12.4f}")
print(f"{'Avg Lift':<15} {avg_lift[0]:<12.4f} {avg_lift[1]:<12.4f}")