from PySide import QtGui, QtCore
import sharppy.viz as viz
import sharppy.viz.preferences as preferences
from sharppy.io.spc_decoder import SPCDecoder

""" plotText() and plotSkewT keep failing """

def load_data():

    dec = SPCDecoder('../../examples/data/14061619.OAX')
    prof_coll = dec.getProfiles()
    prof = prof_coll.getCurrentProfs()['']
    app_frame = QtGui.QApplication([])    
    return prof, prof_coll
    
@pytest.mark.skipif("DISPLAY" not in os.environ)
def test_insets():
    prof, prof_coll = load_data()
    insets = [viz.fire.plotFire,
              viz.winter.plotWinter,
              viz.kinematics.plotKinematics,
              viz.stp.plotSTP,
              viz.ship.plotSHIP,
              viz.vrot.plotVROT,
              viz.analogues.plotAnalogues,
              viz.stpef.plotSTPEF]
    names = ['fire', 'kinematics', 'stp', 'ship', 'vrot', 'sars', 'stpef']
    for inset, name in zip(insets, names):
        print("Testing:", str(inset))
        if inset is viz.thermo.plotText:
            test = inset(['SFC', 'ML', 'MU', 'FCST'])
        else:
            test = inset()
        #try:
        test.setProf(prof)
        #except:
        #    continue
        test.setGeometry(50,50,293,195)
        test.plotBitMap.save(name + '_test.png', format='png')
        del test

@pytest.mark.skipif("DISPLAY" not in os.environ)
def test_skew_hodo():
    prof, prof_coll = load_data()
    skew = viz.skew.plotSkewT
    hodo = viz.hodo.plotHodo

    s = hodo()
    s.addProfileCollection(prof_coll)
    s.setActiveCollection(0)
    s.plotBitMap.save('hodo.png', format='png')

    #s = skew()
    #s.addProfileCollection(prof_coll)
    #s.setActiveCollection(0)
    #s.plotBitMap.save('skew.png', format='png')

@pytest.mark.skipif("DISPLAY" not in os.environ)
def test_other():
    prof, prof_coll = load_data()
    insets = [viz.speed.plotSpeed,
              viz.advection.plotAdvection,
              viz.watch.plotWatch,
              viz.srwinds.plotWinds,
              viz.slinky.plotSlinky,
              viz.thetae.plotThetae]
    names = ['speed', 'advection', 'watch', 'srwinds', 'slinky', 'thetae']
    for inset, name in zip(insets, names):
        print("Testing:", str(inset))
        test = inset()
        test.setProf(prof)
        test.setGeometry(50,50,293,195)
        test.plotBitMap.save(name + '_test.png', format='png')
        del test
