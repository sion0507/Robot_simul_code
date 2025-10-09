import pybullet as p

def set_wheel_angular(robot, j_left, j_right, w_l, w_r, max_torque = 2.0):
  """ 바퀴 목표 각속도 명령"""
  p.setJointMotorControl2(robot, j_left,  p.VELOCITY_CONTROL, targetVelocity=w_l, force=max_torque) # 조인트 모터 조작하여 바퀴의 각속도 변환하는 함수
  p.setJointMotorControl2(robot, j_right, p.VELOCITY_CONTROL, targetVelocity=w_r, force=max_torque)
  # 원하는 속도까지 조정, 위치까지 조정, 토크 조정등 다양한 옵션 존재, force = 목표 각속도까지 올리는데 사용할 힘(모터의 최대 출력)