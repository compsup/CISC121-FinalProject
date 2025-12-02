# Copyright Lauren McQuat 2025
# Code written for CISC 121 Final Assignment @ Queen's University 2025

import gradio as gr
import matplotlib.pyplot as plt
import random

NUM_OF_ELEMENTS = 10


def gen_set(state_data: dict):
    data = sorted([random.randint(1, 100) for _ in range(NUM_OF_ELEMENTS)])
    state_data.update(
        {"data": data, "target": None, "low": 0, "high": len(data) - 1, "mid": None}
    )
    return data


def gen_plot(state_data, found=None):
    data = state_data["data"]
    low, high, mid = state_data["low"], state_data["high"], state_data["mid"]
    # create figure
    if found == -1:
        # Number does not exist in array so we make all bars red
        colours = ["red"] * NUM_OF_ELEMENTS
    else:
        colours = ["skyblue"] * NUM_OF_ELEMENTS
        if found is not None:
            colours[found] = "green"
        else:
            colours[low] = colours[high] = "gray"
            colours[mid] = "yellow"

    fig, ax = plt.subplots()
    ax.bar(range(len(data)), data, color=colours)
    ax.set(xlabel="Index", ylabel="Value", title="Binary Search")
    plt.close(fig)

    return fig


def run_step(state_data, text_box_target):
    data = state_data["data"]
    if data is None:
        raise gr.Error(
            "Please generate a set first!", duration=5, print_exception=False
        )

    if state_data["target"] is None:
        if not isinstance(text_box_target, int):
            raise gr.Error("Please enter only a integer!", print_exception=False)
        state_data["target"] = text_box_target

    target = state_data["target"]
    low, high = state_data["low"], state_data["high"]

    # algorithm implementation

    state_data["mid"] = mid = (high + low) // 2

    if not low <= high:
        return gen_plot(state_data, -1), f"Number does not exist in array!"

    if target == data[mid]:
        return gen_plot(state_data, found=mid), f"{target} found at index {mid}"

    plot = gen_plot(state_data)

    if target > data[mid]:
        # target is higher then mid
        state_data["low"] = mid + 1
    else:
        # target is lower then mid
        state_data["high"] = mid - 1
    return plot, f"Low: {low} High: {high} Mid: {mid}"

def build_ui():
    with gr.Blocks(title="Binary Search") as ui:
        state_data = gr.State(
            {"data": None, "target": None, "low": 0, "high": None, "mid": None}
        )
        gr.Markdown(
            """
        ## Binary Search Visualization
        1. Select Generate Numbers
        2. Input the number you want to search for
        2. Click on step until the number is found
        """
        )
        figure = gr.Plot()

        with gr.Row():
            step_btn = gr.Button("Step", variant="primary")
            gen_set_btn = gr.Button("Generate numbers", variant="secondary")
        
        gen_set_text = gr.Textbox(label="Generated List To Search")
        target = gr.Number(precision=0, value=0)
        output_text = gr.Textbox(label="")

        gen_set_btn.click(gen_set, inputs=[state_data], outputs=gen_set_text)
        step_btn.click(
            run_step, inputs=[state_data, target], outputs=[figure, output_text]
        )
    ui.launch()


if __name__ == "__main__":
    build_ui()
