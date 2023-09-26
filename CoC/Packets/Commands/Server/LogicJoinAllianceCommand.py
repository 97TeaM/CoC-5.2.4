from Utils.Writer import Writer


class LogicJoinAllanceCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.commandID = 1

    def encode(self):

        self.writeInt(0)  # AllianceHighID
        self.writeInt(1)  # AllianceLowID

        self.writeString("SolarLand")  # AllianceName

        self.writeInt(13000000)  # AllianceBadge

        self.writeInt(0)  # AllianceType