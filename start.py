from manim import *
import numpy as np
import shutil

shutil.rmtree("media")


# Define a function to generate Brownian noise
def generate_brownian_motion(T, N):
    dt = T / N
    t = np.linspace(-T, T, N + 1)
    dW = np.sqrt(dt) * np.random.randn(N + 1)  # Corrected the size to N + 1
    W = np.cumsum(dW)

    frequency = 6 * np.pi
    amplitude = 1

    S = amplitude * np.sin(frequency * t)
    return t, S


class BrownianMotion(Scene):
    def construct(self):
        # Parameters
        T = 5.0  # Total time
        N = 100  # Number of time steps

        # Generate Brownian noise
        t, W = generate_brownian_motion(T, N)

        # Create the axes
        axes_factor = 1.2
        axes = Axes(
            x_range=[axes_factor * np.min(t), axes_factor * np.max(t)],
            y_range=[axes_factor * np.min(W), axes_factor * np.max(W)],
            axis_config={"color": BLUE, "include_numbers": True},
        )

        # Create the graph
        graph = self.plot_brownian_motion(t, W, axes)

        # Add the graph and axes to the scene
        self.play(Create(axes))
        self.wait()
        self.play(Create(graph), run_time=10)
        self.wait()

    def plot_brownian_motion(self, t, W, axes):
        points = [(t[i], W[i]) for i in range(len(t))]
        path = VMobject()
        path.set_points_smoothly([axes.c2p(*point) for point in points])
        path.set_color(RED)

        return path
