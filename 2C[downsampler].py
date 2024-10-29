from matplotlib import pyplot as plt

input_signal=[1,2,3,4,5,6]
output_signal=[]

factor=2
for i in input_signal:
    if(i%2!=0):
        output_signal.append(i)
print(output_signal)
plt.subplot(2,1,1)
plt.stem(input_signal)
plt.subplot(2,1,2)
plt.stem(output_signal)

plt.show()