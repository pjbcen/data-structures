from ont_fast5_api.fast5_interface import get_fast5_file

def print_all_raw_data():
  fast5_filepath = "5210_N128870_20170307_FN2002033683_MN19691_sequencing_run_Klebs_Ecoli_HI_barcode_68474_ch2_read3121_strand.fast5" 
  with get_fast5_file(fast5_filepath, mode="r") as f5:
    for read in f5.get_reads():
      raw_data = read.get_raw_data()
      #print(raw_data)
  for i in range(len(raw_data)):
    print(raw_data[i])
  print(len(raw_data))

print_all_raw_data()
