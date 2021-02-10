'''
Created on 22 Oct 2018
Updated 29 Jan 2021

@author: thomasgumbricht
'''

# Package application imports

#from layout import mj_legends as mj_legends

class ProcessLayout():
    '''
    '''
    
    def __init__(self, pp, session):
        '''
        '''
        
        self.session = session
                
        self.pp = pp  
        
        self.verbose = self.pp.process.verbose   
        
        self.session._SetVerbosity(self.verbose)     
        
        # Direct to subprocess
 
        if self.verbose > 1:
            
            print ('    Starting ProcessLayout: ',self.pp.process.processid )
            
        if self.pp.process.processid == 'AddRasterPalette':
            
            self._AddRasterPalette()
            
        elif self.pp.process.processid == 'CreateLegend':
            
            self._AddRasterLegend()
            
        elif self.pp.process.processid == 'CreateScaling':
            
            self._AddRasterScaling()
            
        elif self.pp.process.processid == 'ExportLegend':
            
            self._ExportRasterLegend()
        
        elif self.pp.process.processid == 'AddMovieClock':
            
            self._AddMovieClock()
            
        elif self.process.proc.processid.lower() == 'MovieClock':
            
            self._MovieClock()
            
        else:
            
            exitstr = 'ProcessLayout process %s not available' %(self.process.proc.processid)
            
            exit(exitstr)
            
    def _AddRasterPalette(self):
        '''
        '''
        
        # Convert the parameters to a dict [palette, compid, access, default, setcolor]
        queryD = dict( list( self.pp.process.parameters.__dict__.items() ) )
        
        # pop the setcolor key
        queryD.pop('setcolor')
        
        defaultPalette = queryD.pop('default')
        
        # Set the user as the owner
        queryD['owner'] = self.pp.userproject.userid
        
        colorD = {}
        
        # Loop over all setcolor entries
        paletteD =  dict( list( self.pp.process.parameters.setcolor.__dict__.items() ) )
        
        for key in paletteD:
            
            colorD[key] = dict (list (paletteD[key].__dict__.items() ) )
            
            #queryD['value'] = int(key)
            
            #queryD['owner'] = self.pp.userproject.userid
            
            #for k,v in paramsD.items():
                
            #    queryD[k] = v 
                            
        self.session._ManageRasterPalette(queryD, colorD,
                    self.pp.process.overwrite,self.pp.process.delete)
             
    def _AddRasterLegend(self):
        '''
        '''
        
        # Convert the parameters to a dict 
        queryD = dict( list( self.pp.process.parameters.__dict__.items() ) )
        
        for comp in self.pp.process.comp:
            
            compD = dict( list( comp.__dict__.items() ) )
            
            self.session._ManageRasterLegend(queryD, compD,
                        self.pp.process.overwrite ,self.pp.process.delete)
        
    def _AddRasterScaling(self):
        '''
        '''

        # Convert the parameters to a dict:  
        paramsD =  dict( list( self.pp.process.parameters.__dict__.items() ) )
        
        # CLoop over the compositions
        for comp in self.pp.process.comp:
            
            # Convert each composition to a dict
            d =  dict( list( comp.__dict__.items() ) )
            
            for k in d:
                
                compD = dict( list( d[k].__dict__.items() ) )
        
            # Add to database
            self.session._ManageRasterScaling(paramsD,
                        compD,self.pp.process.overwrite,self.pp.process.delete)
            
    def _AddMovieClock(self):
        '''
        '''
        
        # Convert the parameters to a dict:  
        paramsD =  dict( list( self.pp.process.parameters.__dict__.items() ) )
        
        self.session._ManageMovieClock(paramsD,
                self.pp.process.overwrite, self.pp.process.delete)
    
    def _ExportRasterLegend(self):
        '''
        '''
        exitstr = 'layout.layout.ProcessLaout._ExportRasterLegend not yet implemented'
        
        exit (exitstr)

        #mj_legends.Legend(self.process, self.session)
    
    
        
    def _MovieClock(self):
        '''
        '''
        exitstr = 'layout.layout.ProcessLaout._MovieClock not yet implemented'
        
        exit (exitstr)

        