import os
import sys

# 入力PDFのパスワードを解除し，指定の出力先に出力
def decrypt_pdf_file (input_path, output_path, password):
  tmp = os.system('qpdf --decrypt --password={2} {0} {1}'.format(input_path, output_path, password))

# 入力ディレクトリ内の全PDFのパスワードを解除し，指定の出力先に出力
def decrypt_pdf_files (input_dir, output_dir, password):
  # 指定したディレクトリのファイル名のリストを取得
  filenames = os.listdir(input_dir)
  # 取得したリストから，pdfファイルを取得
  for filename in filenames:
    # filename の拡張子がpdfでなければ continue
    if not filename[-4:] == '.pdf':
      continue
    ipath = '{0}/{1}'.format(input_dir, filename)
    opath = '{0}/{1}'.format(output_dir, filename)
    decrypt_pdf_file(ipath, opath, password)

def wanna_stop (message):
  while True:
    print('{0}[Y/n]'.format(message))
    reply = input()
    if reply == 'n':
      return True
    elif reply == '':
      return False

def main (input_dir, output_dir, password):
  # 出力先ディレクトリがなければ作成
  if not os.path.isdir(output_dir):
    os.mkdir(output_dir)
  # 入力ディレクトリ内のpdfの暗号を全て解除
  decrypt_pdf_files(input_dir, output_dir, password)

if __name__ == '__main__':
  argvs = sys.argv
  if len(argvs) < 3:
    print('引数が足りません．以下の形式で実行してください．')
    print('python decrypt_pdf.py $dir_path $password')
    exit()
  input_dir = argvs[1]
  output_dir = '{0}_decrypted'.format(input_dir)
  password = argvs[2]
  main(input_dir, output_dir, password)
