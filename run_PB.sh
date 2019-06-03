export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export CUDA_VISIBLE_DEVICES=1

log_name=log_PB_self10
file1=PB/PB-Unlabeled.same12.out2
file2=PB/PB-Unlabeled.same12.out
#file3=PB/PB-Unlabeled.same23.out4
#file4=PB/PB-Unlabeled.same23.out5
#file5=PB/PB-Unlabeled.same23.out1
#file6=PB/PB-Unlabeled.same23.out6
nohup python3 -u driver/TrainTestWithLabelled.py --config_file PB.parser.cfg --thread 1 --use-cuda --use_pretrain --labelled_file $file1 $file2 > $log_name 2>&1 &
#nohup /home/lx/anaconda3/bin/python3 -u driver/TrainTest.py --config_file ZX.parser.cfg.2 --thread 1 --use-cuda > $log_name 2>&1 &
tail -f $log_name 
