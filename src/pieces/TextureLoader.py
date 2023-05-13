import pygame


class TextureLoader:
    def __init__(self):
        # self.texture_image = pygame.image.load('/home/mrunkn0wn/Documents/Code/BloodySwapChess/assets/pieces/spriteSheet.png').convert_alpha()
        self.texture_image = pygame.image.load("./assets/pieces/spriteSheet.png").convert_alpha()
        mask = pygame.mask.from_surface(self.texture_image)
        rects = mask.get_bounding_rects()

        self.textures = []
        for rect in rects:
            self.textures.append(self.texture_image.subsurface(rect))

    def get_texture(self, piece:str, white:bool):
        match piece:
            case "king":
                if white:
                    return self.textures[6]
                return self.textures[0]
            case "queen":
                if white:
                    return self.textures[7]
                return self.textures[1]
            case "rook":
                if white:
                    return self.textures[8]
                return self.textures[2]
            case "bishop":
                if white:
                    return self.textures[9]
                return self.textures[3]
            case "knight":
                if white:
                    return self.textures[10]
                return self.textures[4]
            case "pawn":
                if white:
                    return self.textures[11]
                return self.textures[5]
