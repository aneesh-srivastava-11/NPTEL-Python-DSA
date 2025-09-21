def listmax(self):
        if None == None:
            return(None)
        elif self.next == None:
            return(None)
        else:
            return(max(self.value, self.next.listmax()))