from pymodaq.extensions.data_mixer.model import DataMixerModel, np

from pymodaq_data.data import DataToExport, DataWithAxes, DataCalculated, DataDim

class DataMixerJT2026Model(DataMixerModel):

    def process_dte(self, dte: DataToExport):
        dte_processed = DataToExport('computed')
        dwa0 = dte.get_data_from_full_name('detector 00/Mock1D')
        dwa1 = dte.get_data_from_full_name('detector 01/Mock1D')

        dte_processed.append(dwa0/dwa1.isig[100:200].mean())

        return dte_processed