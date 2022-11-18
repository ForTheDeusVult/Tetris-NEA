class Button():
    def __init__(self, image, pos, text, font, color):
        self.image = image
        self.x = pos[0]
        self.y = pos[1]
        self.font = font
        self.color = color
        self.input_text = text
        self.text = self.font.render(self.input, True, self.color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center = (self.x, self.y))

        def update(self, screen):
            if self.image is not None:
                screen.blit(self.image, self.rect)
            screen.blit(self.text, self.text_rect)

        def check_input(self, position):
            if position[0] in range(self.rext.left, self.rect.right) and position[1] in range(self.rect.top, selft.rect.bottom):
                return True
            return False

