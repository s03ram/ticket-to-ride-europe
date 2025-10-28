class Route:
    def __init__(self, start: str, end: str, length: int, color: str, locomotive: int, tunnel: bool):
        self.start = start
        self.end = end
        self.length = length
        self.color = color
        self.locomotive = locomotive
        self.tunnel = tunnel

    def __repr__(self):
        return f"Route({self.start} to {self.end}, Length: {self.length}, Color: {self.color}, Locomotive: {self.locomotive}, Tunnel: {self.tunnel})"

    def get_start(self) -> str:
        """Get the starting city of the route"""
        return self.start

    def get_end(self) -> str:
        """Get the ending city of the route"""
        return self.end

    def get_length(self) -> int:
        """Get the length of the route"""
        return self.length

    def get_color(self) -> str:
        """Get the color of the route"""
        return self.color

    def get_locomotive(self) -> int:
        """Get the number of locomotives required for the route"""
        return self.locomotive

    def is_tunnel(self) -> bool:
        """Check if the route is a tunnel"""
        return self.tunnel