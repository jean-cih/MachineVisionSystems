import matplotlib.pyplot as plt


def create_section_plot(ax, x_data: list, y_data: list, title: str):

    ax.plot(x_data, y_data, marker='o')

    ax.set_title(title)

    ax.set_xticks(x_data)

    ax.grid(True)

    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.text(-0.05, 0.5, 'x', transform=ax.transAxes, ha='right', va='center', rotation=90)
    ax.text(0.5, -0.05, 'y', transform=ax.transAxes, ha='center', va='top')


if __name__ == '__main__':

    x = list(range(-4, 5))
    y_data = [
        [0, 1, 1, -2, 2, 0, -1, -1, 0],
        [0, 0, -2, 2, 4, 0, 0, -4, 0],
        [0, -1, 0, 0, 0, -2, 2, 1, 0],
        [0, 0, -2, 2, 0, 2, -2, 0, 0],
        [0, -1, 0, 1, 0, 1, 0, -1, 0]
    ]

    fig, axes = plt.subplots(5, figsize=(8, 20))

    for i in range(5):
        create_section_plot(axes[i], x, y_data[i], f"Сечение {i+1}")

    plt.tight_layout()
    plt.subplots_adjust(hspace=0.5, top=0.97)

    plt.show()

