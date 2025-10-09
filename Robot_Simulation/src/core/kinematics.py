# 기구 파라미터 (config로 빼도 됨)
R = 0.05  # wheel radius [m]
L = 0.18  # track width [m]

def v_omega_to_wheels(v, omega):
  """로봇 선속도 v, 회전각속도 omega → (왼쪽, 오른쪽) 바퀴 각속도(rad/s)"""
  v_l = v - (L/2)*omega
  v_r = v + (L/2)*omega
  w_l = v_l/R
  w_r = v_r/R
  return w_l, w_r
