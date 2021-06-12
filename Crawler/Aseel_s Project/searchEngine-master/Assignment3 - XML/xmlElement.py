class XmlElement:

    def __init__(self, name, parent=None, children=[], attributes={}, text=""):
        self.name = name
        self.parent = parent
        self.children = children
        self.attributes = attributes
        self.text = text

    def getName(self): 
        return self.name 

    def getParent(self): 
        return self.parent 

    def getChildren(self): 
        return self.children 
    
    def getAttributes(self): 
        return self.attributes 
    
    def getText(self): 
        return self.text 

    def setName(self, name): 
        self.name = name 

    def setParent(self, parent): 
        self.name = parent 
    
    def setChildren(self, children): 
        self.children = children 
    
    def setAttributes(self, attributes): 
        self.attributes = attributes 
    
    def setText(self, text): 
        self.text = text 

    def addChild(self, child): 
        self.children.append(child) 

    def toString(self):
        print("Name: " + str(self.name) + "\n" + "Parent: " + str(self.parent) + "\n" + "Children: " +
              str(self.children) + "\n" + "Attributes: " + str(self.attributes) + "\n" + "Text: " + str(self.text) + "\n")

