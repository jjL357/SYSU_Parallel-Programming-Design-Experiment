import matplotlib.pyplot as plt

# Thread block sizes
thread_block_sizes = [4, 8, 16, 32, 64]

# Time for convolution (ms)
times = [6.52, 17.28, 22.07, 41.44, 0.01]

plt.figure(figsize=(8, 6))
plt.plot(thread_block_sizes, times, marker='o', linestyle='-', color='b', linewidth=2)

plt.title('Time for Convolution vs. Thread Block Size')
plt.xlabel('Thread Block Size')
plt.ylabel('Time for Convolution (ms)')
plt.grid(True)
plt.xticks(thread_block_sizes)
plt.yticks(range(0, 50, 5))
plt.tight_layout()

plt.show()
