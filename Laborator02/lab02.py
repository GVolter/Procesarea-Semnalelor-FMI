import numpy as np
import matplotlib.pyplot as plt
import scipy

def ex1():
    ampl = 1
    freq = 2
    phase_sin = 0

    phase_cos = phase_sin + (np.pi / 2)

    fs = 44100
    duration = 2.0        
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)  

    sin_wave = ampl * np.sin(2 * np.pi * freq * t + phase_sin)
    cos_wave = ampl * np.cos(2 * np.pi * freq * t - phase_cos)

    fig, axs = plt.subplots(2, 1, figsize=(10, 6))

    axs[0].plot(t, sin_wave, label='Semnal sinusoidal')
    axs[0].set_title('Semnal sinusoidal')
    axs[0].set_xlabel('Timp')
    axs[0].set_ylabel('Amplitudine')
    axs[0].grid(True)
    axs[0].legend()

    axs[1].plot(t, cos_wave, label='Semnal cosinus', linestyle='dashed', color='r')
    axs[1].set_title('Semnal cosinus')
    axs[1].set_xlabel('Timp')
    axs[1].set_ylabel('Amplitudine')
    axs[1].grid(True)
    axs[1].legend()

    # plt.plot(t, sin_wave)
    # plt.suptitle('Semnal sinusoidal si cosinus')
    # plt.plot(t, cos_wave, linestyle='dashed', color='r')
    plt.tight_layout()
    plt.show()

def add_noise(x, snr):
    X = np.linalg.norm(x)**2 / x.size
    noise_power = X / snr
    z = np.random.randn(x.size) 
    y = np.sqrt(noise_power) * z / np.linalg.norm(z)

    return x + y

def ex2():
    freq = 5
    phase = [0, 2, 4, 6]
    SNR = [0.1, 1, 10, 100]

    fs = 100
    duration = 0.5       
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)  

    for ph in phase:
        sin_wave = np.sin(2 * np.pi * freq * t + ph)

        for snr in SNR:
            noisy_signal = add_noise(sin_wave, snr)
            plt.plot(t, noisy_signal, label=f'SNR: {snr}')
        
        plt.title(f'Faza: {ph}')
        plt.grid(True)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    # ex1()
    ex2()